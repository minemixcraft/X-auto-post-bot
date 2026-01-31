import os
import time
import random
import tweepy
from datetime import datetime, timezone, timedelta

# 🔥 IMPORT UI MODULE
import bot_ui_text as bot_ui 
# import bot_ui as bot_ui

# ======================================================
# 1. TIME & SCHEDULE
# ======================================================
def get_thai_time():
    return datetime.now(timezone.utc) + timedelta(hours=7)

def get_seconds_until_target(now, target_hour):
    target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    return (target_time - now).total_seconds()

def get_schedule_context(current_hour):
    if current_hour < 10:
        return {"name": "Morning Round", "msg_index": 0, "max_wait_min": 45, "target_hour": 8, "upload_image": True}
    elif current_hour < 15:
        return {"name": "Afternoon Round", "msg_index": 1, "max_wait_min": 60, "target_hour": 12, "upload_image": False}
    else:
        return {"name": "Evening Round", "msg_index": 2, "max_wait_min": 90, "target_hour": 17, "upload_image": False}

# ======================================================
# 2. WAIT & DELAY
# ======================================================
def execute_sleep_with_progress(total_wait_seconds):
    effective_wait = max(0, total_wait_seconds - 60)
    if effective_wait < 10: 
        time.sleep(effective_wait)
        return

    chunk_size = effective_wait / 10
    print(f"   Timer Started: {bot_ui.format_time_str(effective_wait)} remaining.")
    
    for i in range(1, 11):
        time.sleep(chunk_size)
        percent = i * 10
        remaining = effective_wait - (chunk_size * i)
        is_done = (i == 10)
        bot_ui.print_waiting_bar(percent, remaining, is_finished=is_done)

def wait_for_schedule_start(target_hour):
    bot_ui.print_section_header("⏳ [WAITING PROCESS]")
    while True:
        now = get_thai_time()
        if now.hour >= target_hour:
            break 
        wait_seconds = get_seconds_until_target(now, target_hour)
        if wait_seconds > 0:
            execute_sleep_with_progress(wait_seconds)
            break 
        else:
            time.sleep(30)
    bot_ui.print_closer()

def apply_random_delay(max_wait_min):
    if max_wait_min > 0:
        bot_ui.print_section_header("🚀 [EXECUTION START]")
        wait_sec = random.randint(60, max_wait_min * 60)
        bot_ui.print_info("Strategy", f"Random Delay ({wait_sec // 60}m {wait_sec % 60}s)")
        print("   ... (Sleeping) ...")
        
        chunk_size = wait_sec / 10
        for i in range(1, 11):
            time.sleep(chunk_size)
            percent = i * 10
            remaining = max(0, wait_sec - (chunk_size * i))
            is_done = (i == 10)
            status = "Waking Up!" if is_done else "Sleeping..."
            bot_ui.print_waiting_bar(percent, remaining, is_finished=is_done, custom_status=status)
        bot_ui.print_closer()

# ======================================================
# 3. CONTENT & API
# ======================================================
def prepare_message(msg_index, messages_list, hashtag_pool):
    if msg_index >= len(messages_list): msg_index = 0
    base_msg = messages_list[msg_index].strip() + "\n\n"
    tags = list(set(hashtag_pool))
    random.shuffle(tags)
    final_msg = base_msg
    for t in tags:
        if len(final_msg + t + " ") <= 280: final_msg += t + " "
        else: break 
    return final_msg.strip()

def get_twitter_client():
    keys = [os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"), os.getenv("X_ACCESS_TOKEN"), os.getenv("X_ACCESS_TOKEN_SECRET")]
    if not all(keys): raise ValueError("Missing API Keys")
    return tweepy.Client(consumer_key=keys[0], consumer_secret=keys[1], access_token=keys[2], access_token_secret=keys[3]), tweepy.API(tweepy.OAuth1UserHandler(keys[0], keys[1], keys[2], keys[3]))

def upload_images(api_v1, image_paths):
    media_ids = []
    # 1. แสดง Header Uploading
    bot_ui.print_upload_header()
    
    valid_images = [img for img in image_paths if os.path.exists(img)]
    bot_ui.print_media_found(len(valid_images))

    for img_path in valid_images:
        try:
            upload = api_v1.media_upload(filename=img_path)
            media_ids.append(upload.media_id)
            # 2. แสดง item ที่อัปโหลด
            bot_ui.print_upload_item(os.path.basename(img_path), upload.media_id)
        except Exception as e:
            bot_ui.print_upload_error(img_path, e)
            
    # 3. ปิดเส้น Uploading
    bot_ui.print_closer()
    return media_ids

def post_tweet(client, message, media_ids=None):
    # 1. แสดง Header POSE
    bot_ui.print_pose_header()
    
    if not media_ids: media_ids = None 
    try:
        response = client.create_tweet(text=message, media_ids=media_ids)
        # 2. แสดง Success
        bot_ui.print_post_success(response.data['id'])
    except Exception as e:
        print(f"   ❌ Failed to tweet: {e}")
    
    # 3. ปิดเส้น POSE
    bot_ui.print_closer()

# ======================================================
# 4. MAIN FLOW
# ======================================================
def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    bot_ui.print_header(bot_name)

    try:
        start_time = get_thai_time()
        context = get_schedule_context(start_time.hour)
        
        # System Check
        bot_ui.print_system_check(context['name'], f"{context['target_hour']}:00", context['upload_image'])

        # Wait
        wait_for_schedule_start(context['target_hour'])

        # Random Delay
        # apply_random_delay(context['max_wait_min'])
        apply_random_delay(1)
        

        # Prepare Content
        client, api_v1 = get_twitter_client()
        message = prepare_message(context['msg_index'], bot_data["messages"], hashtag_pool)
        
        # --- PREVIEW SECTION ---
        bot_ui.print_preview_box(message)

        # --- UPLOAD SECTION ---
        media_ids = []
        if context['upload_image'] and "images" in bot_data:
            media_ids = upload_images(api_v1, bot_data["images"])
        else:
            # กรณีไม่มีรูป ก็ให้แสดง Section ว่างๆ หรือข้ามไป (ตาม Logic เดิมคือข้าม แต่ถ้าอยากให้โชว์ก็ได้)
            # เอาตาม Logic เดิมคือถ้าไม่มีรูปก็ไม่เข้า function upload
            pass

        # --- POST SECTION ---
        post_tweet(client, message, media_ids)

    except Exception as e:
        print("\n" + "!"*50)
        print(f"❌ CRITICAL SYSTEM ERROR: {e}")
        print("!"*50)
    
    # --- END SECTION ---
    bot_ui.print_end()


