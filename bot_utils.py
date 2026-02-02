import os
import time
import random
import tweepy
import re
import importlib
from datetime import datetime, timezone, timedelta

# 🔥 IMPORT CONFIG
from bot_config import SCHEDULE_CONFIG, SYSTEM_CONFIG, TWITTER_LIMITS, UI_CONFIG

# 🔥 DYNAMIC UI LOADING
ui_module_name = UI_CONFIG.get("MODULE_NAME", "bot_ui_text")
try:
    bot_ui = importlib.import_module(ui_module_name)
    # print(f"✅ Loaded UI Module: {ui_module_name}") # ปิดไว้เพื่อให้หน้าจอสะอาด
except ImportError:
    print(f"❌ Error: Could not load UI module '{ui_module_name}'. Falling back to 'bot_ui_text'.")
    import bot_ui_text as bot_ui

# ======================================================
# 1. PURE LOGIC & CALCULATIONS
# ======================================================

def get_thai_time():
    """คืนค่าเวลาปัจจุบัน (ตาม Config Timezone)"""
    offset = SYSTEM_CONFIG.get("TIMEZONE_HOURS", 7)
    return datetime.now(timezone.utc) + timedelta(hours=offset)

def get_seconds_until_target(now, target_hour):
    target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    return (target_time - now).total_seconds()

def get_schedule_context(current_hour):
    if current_hour < SCHEDULE_CONFIG["MORNING"]["CUTOFF_HOUR"]:
        cfg = SCHEDULE_CONFIG["MORNING"]
    elif current_hour < SCHEDULE_CONFIG["AFTERNOON"]["CUTOFF_HOUR"]:
        cfg = SCHEDULE_CONFIG["AFTERNOON"]
    else:
        cfg = SCHEDULE_CONFIG["EVENING"]
    
    return {
        "name": cfg["NAME"],
        "msg_index": cfg["MSG_INDEX"],
        "max_wait_min": cfg["MAX_WAIT_MIN"],
        "target_hour": cfg["TARGET_HOUR"],
        "upload_image": cfg["UPLOAD_IMAGE"]
    }

def calculate_time_budget(start_time, max_runtime_min):
    elapsed_sec = time.time() - start_time
    remaining_sec = (max_runtime_min * 60) - elapsed_sec
    return elapsed_sec / 60, remaining_sec / 60

def calculate_safe_delay(config_delay_min, remaining_min):
    if remaining_min <= 0: return 0
    safe_delay = min(config_delay_min, remaining_min)
    return safe_delay if safe_delay >= 1 else 0

def analyze_tweet_weight(text):
    """วิเคราะห์น้ำหนักโดยใช้ค่าจาก TWITTER_LIMITS ใน Config"""
    url_pattern = r'https?://\S+|www\.\S+|lin\.ee/\S+'
    urls = re.findall(url_pattern, text)
    text_without_urls = re.sub(url_pattern, '', text)
    
    LINK_W = TWITTER_LIMITS["URL_WEIGHT"]
    EMOJI_W = TWITTER_LIMITS["EMOJI_WEIGHT"]
    THAI_W = TWITTER_LIMITS["THAI_WEIGHT"]
    
    stats = {
        "link_count": len(urls),
        "link_weight": len(urls) * LINK_W,
        "emoji_count": 0, "emoji_weight": 0,
        "text_count": 0, "text_weight": 0,
        "space_count": 0, "space_weight": 0,
        "total_weight": 0
    }
    
    for char in text_without_urls:
        code = ord(char)
        if char.isspace():
            stats['space_count'] += 1
            stats['space_weight'] += 1
        elif (0x0E00 <= code <= 0x0E7F): # Thai
            stats['text_count'] += 1
            stats['text_weight'] += THAI_W
        elif (code <= 127): # ASCII
            stats['text_count'] += 1
            stats['text_weight'] += 1
        else: # Emoji/Special
            stats['emoji_count'] += 1
            stats['emoji_weight'] += EMOJI_W
            
    stats['total_weight'] = (stats['link_weight'] + stats['emoji_weight'] + 
                             stats['text_weight'] + stats['space_weight'])
    return stats

def calculate_x_char_weight(text):
    return analyze_tweet_weight(text)['total_weight']

def prepare_tweet_content(msg_index, messages_list, hashtag_pool):
    if not messages_list: return ""
    if msg_index >= len(messages_list): msg_index = 0
    
    base_msg = messages_list[msg_index].strip() + "\n\n"
    tags = list(set(hashtag_pool))
    random.shuffle(tags)
    
    final_msg = base_msg
    MAX_CHARS = TWITTER_LIMITS["MAX_CHARS"]
    
    for t in tags:
        test_msg = final_msg + t + " "
        if calculate_x_char_weight(test_msg) <= MAX_CHARS:
            final_msg = test_msg
        else:
            break
    return final_msg.strip()

def filter_existing_images(image_paths):
    if not image_paths: return []
    return [img for img in image_paths if os.path.exists(img)]

# ======================================================
# 2. LOW-LEVEL ACTIONS
# ======================================================
def get_twitter_api():
    keys = [os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"), os.getenv("X_ACCESS_TOKEN"), os.getenv("X_ACCESS_TOKEN_SECRET")]
    if not all(keys): raise ValueError("Missing API Keys")
    
    client = tweepy.Client(consumer_key=keys[0], consumer_secret=keys[1], access_token=keys[2], access_token_secret=keys[3])
    auth = tweepy.OAuth1UserHandler(keys[0], keys[1], keys[2], keys[3])
    api_v1 = tweepy.API(auth)
    return client, api_v1

def sleep_with_progress_bar(seconds, start_msg=None, status_msg="Waiting...", end_msg=None):
    if seconds <= 0: return
    effective_wait = max(0, seconds - 60)
    if effective_wait < 10:
        time.sleep(effective_wait)
        return

    if start_msg:
        print(f"   {start_msg}: {bot_ui.format_time_str(effective_wait)} remaining.")

    chunk_size = effective_wait / 10
    for i in range(1, 11):
        time.sleep(chunk_size)
        percent = i * 10
        remaining = effective_wait - (chunk_size * i)
        is_done = (i == 10)
        current_status = end_msg if (is_done and end_msg) else status_msg
        bot_ui.print_waiting_bar(percent, remaining, is_finished=is_done, custom_status=current_status)

def upload_single_file(api_v1, filepath):
    if SYSTEM_CONFIG.get("DRY_RUN", False):
        bot_ui.print_upload_item(os.path.basename(filepath), "DRY_RUN_ID")
        return "DRY_RUN_ID"

    try:
        upload = api_v1.media_upload(filename=filepath)
        bot_ui.print_upload_item(os.path.basename(filepath), upload.media_id)
        return upload.media_id
    except Exception as e:
        bot_ui.print_upload_error(filepath, e)
        return None

# ======================================================
# 3. HIGH-LEVEL TASKS & ORCHESTRATOR
# ======================================================

def initialize_bot_session(bot_data, hashtag_pool):
    start_time = get_thai_time()
    context = get_schedule_context(start_time.hour)
    return {
        "start_time": start_time,
        "workflow_start": time.time(),
        "max_runtime_min": SYSTEM_CONFIG.get("MAX_RUNTIME_MIN", 110),
        "context": context,
        "bot_data": bot_data,
        "hashtag_pool": hashtag_pool
    }

def perform_system_check(session):
    ctx = session['context']
    bot_ui.print_system_check(
        context_name=ctx['name'], 
        target_time=f"{ctx['target_hour']}:00",
        current_date=session['start_time'].strftime("%Y-%m-%d"),
        current_time=session['start_time'].strftime("%H:%M:%S"),
        upload_image=ctx['upload_image'],
        msg_count=len(session['bot_data'].get('messages', [])),
        tag_count=len(session['hashtag_pool']),
        max_delay=ctx['max_wait_min']
    )

def wait_until_target_time(session):
    target_hour = session['context']['target_hour']
    bot_ui.print_waiting_header()
    while True:
        now = get_thai_time()
        if now.hour >= target_hour: break 
        wait_seconds = get_seconds_until_target(now, target_hour)
        if wait_seconds > 0:
            sleep_with_progress_bar(wait_seconds, start_msg="Timer Started", status_msg="Waiting...")
            break 
        else:
            time.sleep(30)
    bot_ui.print_closer()

def execute_safety_delay_strategy(session):
    elapsed_min, remaining_min = calculate_time_budget(session['workflow_start'], session['max_runtime_min'])
    config_delay = session['context']['max_wait_min']
    safe_delay = calculate_safe_delay(config_delay, remaining_min)

    bot_ui.print_execution_header()
    bot_ui.print_time_budget(session['max_runtime_min'], elapsed_min, remaining_min, config_delay, safe_delay)

    if safe_delay > 0:
        wait_sec = random.randint(60, int(safe_delay * 60))
        bot_ui.print_strategy_info(wait_sec // 60, wait_sec % 60)
        sleep_with_progress_bar(wait_sec, status_msg="Sleeping...", end_msg="Waking Up!")
    else:
        print("   ➤ Skipped Random Delay (Budget tight or Config 0)")
    bot_ui.print_closer()

def connect_twitter_services():
    return get_twitter_api()

def generate_and_preview_content(session):
    ctx = session['context']
    message = prepare_tweet_content(
        ctx['msg_index'], 
        session['bot_data'].get("messages", []), 
        session['hashtag_pool']
    )
    if UI_CONFIG.get("SHOW_PREVIEW", True):
        weight_stats = analyze_tweet_weight(message)
        bot_ui.print_preview_box(message, weight_stats)
    return message

def handle_media_uploads(api_v1, session):
    ctx = session['context']
    bot_data = session['bot_data']
    bot_ui.print_upload_header()
    media_ids = []
    if ctx['upload_image'] and "images" in bot_data:
        valid_images = filter_existing_images(bot_data["images"])
        bot_ui.print_media_found(len(valid_images))
        for img in valid_images:
            mid = upload_single_file(api_v1, img)
            if mid: media_ids.append(mid)
    bot_ui.print_closer()
    return media_ids

def publish_tweet_to_x(client, message, media_ids):
    bot_ui.print_pose_header()
    
    if SYSTEM_CONFIG.get("DRY_RUN", False):
        print("\n   ⚠️ [DRY RUN MODE ENABLED]")
        print("   ➤ Skipped actual posting to Twitter API")
        post_info = {
            "id": "DRY_RUN_ID_12345",
            "timestamp": get_thai_time().strftime("%Y-%m-%d %H:%M:%S"),
            "url": "https://twitter.com/dry_run/status/00000",
            "media_count": len(media_ids) if media_ids else 0,
            "weight": calculate_x_char_weight(message)
        }
        bot_ui.print_post_success(post_info)
        bot_ui.print_closer()
        return

    try:
        response = client.create_tweet(text=message, media_ids=media_ids)
        tweet_id = response.data['id']
        post_info = {
            "id": tweet_id,
            "timestamp": get_thai_time().strftime("%Y-%m-%d %H:%M:%S"),
            "url": f"https://twitter.com/user/status/{tweet_id}",
            "media_count": len(media_ids) if media_ids else 0,
            "weight": calculate_x_char_weight(message)
        }
        bot_ui.print_post_success(post_info)
    except Exception as e:
        print(f"   ❌ Failed to tweet: {e}")
    bot_ui.print_closer()

def handle_critical_error(e):
    print("\n" + "!"*50)
    print(f"❌ CRITICAL SYSTEM ERROR: {e}")
    print("!"*50)

def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    bot_ui.print_header(bot_name)
    try:
        session = initialize_bot_session(bot_data, hashtag_pool)
        perform_system_check(session)
        wait_until_target_time(session)
        execute_safety_delay_strategy(session)
        client, api_v1 = connect_twitter_services()
        message = generate_and_preview_content(session)
        media_ids = handle_media_uploads(api_v1, session)
        publish_tweet_to_x(client, message, media_ids or None)
    except Exception as e:
        handle_critical_error(e)
    bot_ui.print_end()

def run_manual_workflow(bot_name, bot_data, hashtag_pool):
    """Workflow สำหรับเทส (ข้ามการรอเวลา)"""
    bot_ui.print_header(bot_name)
    try:
        session = initialize_bot_session(bot_data, hashtag_pool)
        perform_system_check(session)
        client, api_v1 = connect_twitter_services()
        message = generate_and_preview_content(session)
        media_ids = handle_media_uploads(api_v1, session)
        publish_tweet_to_x(client, message, media_ids or None)
    except Exception as e:
        handle_critical_error(e)
    bot_ui.print_end()