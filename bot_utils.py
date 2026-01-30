import os
import time
import random
import tweepy
from datetime import datetime, timezone, timedelta

# ======================================================
# 🎨 UI THEME SELECTION
# ======================================================
# เลือกเปิด/ปิด Comment บรรทัดนี้เพื่อสลับธีม

# import bot_ui_text as bot_ui  # ธีม Text (d[o_0]b)
import bot_ui as bot_ui       # ธีม ASCII (Pagga)

# ======================================================
# 1. TIME & SCHEDULE HELPERS
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
# 2. WAITING & DELAY LOGIC
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
        bot_ui.print_shades_bar(percent, remaining, is_finished=is_done)

def wait_for_schedule_start(target_hour):
    bot_ui.print_section("WAITING")
    
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
            
    bot_ui.print_closer() # ✅ เรียกใช้ได้เลย ไม่ต้องเช็ค

def apply_random_delay(max_wait_min):
    if max_wait_min > 0:
        bot_ui.print_section("EXECUTION")
        
        wait_sec = random.randint(60, max_wait_min * 60)
        
        # ส่ง Strategy info
        bot_ui.print_info("Strategy", f"Random Delay ({wait_sec // 60}m {wait_sec % 60}s)")
        print("   ... (Sleeping) ...")
        
        chunk_size = wait_sec / 10
        for i in range(1, 11):
            time.sleep(chunk_size)
            percent = i * 10
            remaining = max(0, wait_sec - (chunk_size * i))
            
            if i == 10:
                bot_ui.print_shades_bar(100, 0, is_finished=True, custom_status="Waking Up!")
            else:
                bot_ui.print_shades_bar(percent, remaining, is_finished=False, custom_status="Sleeping...")
        
        bot_ui.print_closer() # ✅ เรียกใช้ได้เลย

# ======================================================
# 3. LOGGING & DISPLAY HELPER
# ======================================================

def log_system_info(context, start_time, bot_data, hashtag_pool):
    bot_ui.print_section("SYSTEM_CHECK")
    
    bot_ui.print_info("Time Zone", "Asia/Bangkok (UTC+7)")
    bot_ui.print_info("Context", context['name'])
    bot_ui.print_info("Target Time", f"{context['target_hour']}:00")
    bot_ui.print_info("Current Date", start_time.strftime("%Y-%m-%d"))
    bot_ui.print_info("Has Image?", "Yes" if context['upload_image'] else "No")
    
    print("") 
    
    bot_ui.print_info("Msg Loaded", f"{len(bot_data['messages'])} items")
    bot_ui.print_info("Tag Pool", f"{len(hashtag_pool)} tags")
    bot_ui.print_info("Max Delay", f"{context['max_wait_min']} mins")
    
    bot_ui.print_closer() # ✅ เรียกใช้ได้เลย

# ======================================================
# 4. CONTENT & TWITTER API
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
    bot_ui.print_section("UPLOADING")
    
    valid_images = [img for img in image_paths if os.path.exists(img)]
    bot_ui.print_info("Media Found", f"{len(valid_images)} Images")

    for img_path in valid_images:
        try:
            upload = api_v1.media_upload(filename=img_path)
            media_ids.append(upload.media_id)
            print(f"   ✔ Uploaded      : {os.path.basename(img_path)} [ID: {str(upload.media_id)[:5]}...]")
        except Exception as e:
            bot_ui.print_error(f"Error {img_path}: {e}")
            
    bot_ui.print_closer() # ✅ เรียกใช้ได้เลย
    return media_ids

def post_tweet(client, message, media_ids=None):
    if not media_ids: media_ids = None 
    try:
        # response = client.create_tweet(text=message, media_ids=media_ids) ====================================================== ======================================================
        
        # ปริ้น Success 
        # (ใน bot_ui ASCII จะปริ้นแค่ text ปกติ, ใน bot_ui_text จะปริ้นแบบ section)
        # แต่เรียกชื่อฟังก์ชันเดียวกันได้เลย
        print(f"\n   [TWEET POSTED SUCCESSFULLY]") 
        bot_ui.print_info("Tweet ID", response.data['id'])
        print("")

        return True
    except Exception as e:
        bot_ui.print_error(f"Failed to tweet: {e}")
        return False

# ======================================================
# 5. MAIN WORKFLOW
# ======================================================

def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    bot_ui.print_header(bot_name)

    try:
        start_time = get_thai_time()
        context = get_schedule_context(start_time.hour)
        
        log_system_info(context, start_time, bot_data, hashtag_pool)

        wait_for_schedule_start(0)
        # wait_for_schedule_start(context['target_hour'])====================================================== ======================================================
        

        # apply_random_delay(context['max_wait_min'])====================================================== ======================================================
        apply_random_delay(2)
        

        client, api_v1 = get_twitter_client()
        message = prepare_message(context['msg_index'], bot_data["messages"], hashtag_pool)
        
        bot_ui.print_preview_box(message)

        media_ids = []
        if context['upload_image'] and "images" in bot_data:
            media_ids = upload_images(api_v1, bot_data["images"])

        post_tweet(client, message, media_ids)

    except Exception as e:
        print("\n" + "!"*50)
        bot_ui.print_error(f"CRITICAL SYSTEM ERROR: {e}")
        print("!"*50)
    
    bot_ui.print_footer()
