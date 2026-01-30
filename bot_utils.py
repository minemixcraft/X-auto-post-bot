import os
import time
import math
import random
import tweepy
from datetime import datetime, timezone, timedelta

# 🔥 IMPORT UI MODULE (ดึงกราฟิกมาใช้)
import bot_ui

# ======================================================
# 1. TIME & SCHEDULE
# ======================================================

def get_thai_time():
    return datetime.now(timezone.utc) + timedelta(hours=7)

def get_seconds_until_target(now, target_hour):
    target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    return (target_time - now).total_seconds()

def get_schedule_context(current_hour):
    # ปรับ Logic ตามเวลาที่คุณต้องการ
    if current_hour < 10:
        return {"name": "Morning Round", "msg_index": 0, "max_wait_min": 45, "target_hour": 8, "upload_image": True}
    elif current_hour < 15:
        return {"name": "Afternoon Round", "msg_index": 1, "max_wait_min": 60, "target_hour": 12, "upload_image": False}
    else:
        return {"name": "Evening Round", "msg_index": 2, "max_wait_min": 90, "target_hour": 17, "upload_image": False}

# ======================================================
# 2. LOGIC: WAIT SYSTEM
# ======================================================

def execute_sleep_with_progress(total_wait_seconds):
    effective_wait = max(0, total_wait_seconds - 60)
    
    if effective_wait < 10: 
        time.sleep(effective_wait)
        return

    chunk_size = effective_wait / 10
    
    # ใช้ UI: แสดงเวลาเริ่มต้น
    print(f"   ⏳ Timer Started: {bot_ui.format_time_str(effective_wait)} remaining.")
    
    for i in range(1, 11):
        time.sleep(chunk_size)
        percent = i * 10
        remaining = effective_wait - (chunk_size * i)
        is_done = (i == 10)
        
        # ใช้ UI: แสดง Progress Bar
        bot_ui.print_shades_bar(percent, remaining, is_finished=is_done)

def wait_for_schedule_start(target_hour):
    # ใช้ UI: แสดง Header Waiting
    bot_ui.print_section("WAITING")
    bot_ui.print_info("Action", f"Checking time... Target is {target_hour}:00")
    
    while True:
        now = get_thai_time()
        
        if now.hour >= target_hour:
            print(f"\n   ✅ It's time! ({now.strftime('%H:%M:%S')}) Starting process...")
            break
            
        wait_seconds = get_seconds_until_target(now, target_hour)
        
        if wait_seconds > 0:
            execute_sleep_with_progress(wait_seconds)
        else:
            time.sleep(30)

# ======================================================
# 3. LOGIC: TWITTER API
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
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise ValueError("Missing API Keys")

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api_v1 = tweepy.API(auth)
    return client, api_v1

def upload_images(api_v1, image_paths):
    media_ids = []
    # ใช้ UI: แสดง Header Uploading
    bot_ui.print_section("UPLOADING")
    
    for img_path in image_paths:
        if os.path.exists(img_path):
            try:
                upload = api_v1.media_upload(filename=img_path)
                media_ids.append(upload.media_id)
                # ใช้ UI: Print Success
                bot_ui.print_success(f"Uploaded       : {os.path.basename(img_path)}")
            except Exception as e:
                bot_ui.print_error(f"Error Upload  : {e}")
        else:
            bot_ui.print_error(f"File Missing  : {img_path}")
    return media_ids

def post_tweet(client, message, media_ids=None):
    if not media_ids: media_ids = None 
    try:
        response = client.create_tweet(text=message, media_ids=media_ids)
        bot_ui.print_success(f"Tweet Posted! ID: {response.data['id']}")
        return True
    except Exception as e:
        bot_ui.print_error(f"Failed to tweet: {e}")
        return False

# ======================================================
# 4. MAIN FLOW (ORCHESTRATOR)
# ======================================================

def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    # 1. Header
    bot_ui.print_header(bot_name)

    try:
        start_time = get_thai_time()
        context = get_schedule_context(start_time.hour)
        
        # 2. System Check
        bot_ui.print_section("SYSTEM_CHECK")
        bot_ui.print_info("Context", context['name'])
        bot_ui.print_info("Target Time", f"{context['target_hour']}:00")
        bot_ui.print_info("Has Image?", "Yes" if context['upload_image'] else "No")

        # 3. Wait System (With Art)
        wait_for_schedule_start(context['target_hour'])

        # 4. Random Delay
        if context['max_wait_min'] > 0:
            bot_ui.print_section("EXECUTION")
            wait_sec = random.randint(60, context['max_wait_min'] * 60)
            bot_ui.print_info("Strategy", f"Random Delay {wait_sec // 60}m {wait_sec % 60}s")
            print("   💤 Sleeping...")
            time.sleep(wait_sec)

        # 5. Prepare & Preview
        client, api_v1 = get_twitter_client()
        message = prepare_message(context['msg_index'], bot_data["messages"], hashtag_pool)
        
        bot_ui.print_preview_box(message)

        # 6. Upload Images
        media_ids = []
        if context['upload_image'] and "images" in bot_data:
            media_ids = upload_images(api_v1, bot_data["images"])

        # 7. Post
        # ใช้ UI: แสดง Header ก่อนส่ง
        print("\n" + "-"*40)
        print("[Sending] Posting tweet to X...")
        post_tweet(client, message, media_ids)

    except Exception as e:
        print("\n" + "!"*50)
        bot_ui.print_error(f"CRITICAL SYSTEM ERROR: {e}")
        print("!"*50)
    
    # 8. Footer
    print("\n")
    bot_ui.print_art("COMPLETED")
    print("\n" + "="*50)
