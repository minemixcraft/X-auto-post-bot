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
# 2. LOGIC: WAIT & DELAY
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
    # [STEP 1]
    bot_ui.print_waiting_header()
    
    waited_seconds = 0
    start_wait = time.time() # จับเวลาเริ่มรอ

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
    
    # คืนค่าเวลาที่ใช้ไปทั้งหมดในช่วง Wait
    waited_seconds = time.time() - start_wait
    return waited_seconds

def apply_random_delay(max_wait_min):
    # ฟังก์ชันนี้รับค่า max_wait_min ที่ถูกคำนวณมาอย่างปลอดภัยแล้วจาก Main Flow
    if max_wait_min > 0:
        # [STEP 2]
        bot_ui.print_execution_header()
        
        wait_sec = random.randint(60, int(max_wait_min * 60))
        bot_ui.print_strategy_info(wait_sec // 60, wait_sec % 60)
        
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
# 3. LOGIC: CONTENT & API
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
    # [STEP 3]
    media_ids = []
    bot_ui.print_upload_header()
    
    valid_images = [img for img in image_paths if os.path.exists(img)]
    bot_ui.print_media_found(len(valid_images))

    for img_path in valid_images:
        try:
            upload = api_v1.media_upload(filename=img_path)
            media_ids.append(upload.media_id)
            bot_ui.print_upload_item(os.path.basename(img_path), upload.media_id)
        except Exception as e:
            bot_ui.print_upload_error(img_path, e)
            
    bot_ui.print_closer()
    return media_ids

def post_tweet(client, message, media_ids=None):
    # [STEP 4]
    bot_ui.print_pose_header()
    
    if not media_ids: media_ids = None 
    try:
        response = client.create_tweet(text=message, media_ids=media_ids)
        bot_ui.print_post_success(response.data['id'])
    except Exception as e:
        print(f"   ❌ Failed to tweet: {e}")
    
    bot_ui.print_closer()

# ======================================================
# 4. MAIN FLOW (Safety Logic Added)
# ======================================================
def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    bot_ui.print_header(bot_name)
    
    # 🔥 จับเวลาเริ่ม Workflow (GitHub Limit 2 ชั่วโมง)
    workflow_start_time = time.time()
    MAX_RUNTIME_SEC = 110 * 60  # ตั้งเป้าจบใน 110 นาที (เผื่อ Buffer 10 นาที)

    try:
        start_time = get_thai_time()
        context = get_schedule_context(start_time.hour)
        
        # SYSTEM CHECK
        bot_ui.print_system_check(
            context_name=context['name'], 
            target_time=f"{context['target_hour']}:00",
            current_date=start_time.strftime("%Y-%m-%d"),
            current_time=start_time.strftime("%H:%M:%S"),
            upload_image=context['upload_image'],
            msg_count=len(bot_data['messages']),
            tag_count=len(hashtag_pool),
            max_delay=context['max_wait_min']
        )

        # 1. รอเวลาตามเป้าหมาย (Wait System)
        # รับค่ากลับมาว่าใช้เวลาไปเท่าไหร่
        waited_sec = wait_for_schedule_start(context['target_hour'])

        # 2. คำนวณเวลาที่เหลือสำหรับ Random Delay
        # เวลาที่ผ่านไปแล้วทั้งหมด
        elapsed_total = time.time() - workflow_start_time
        
        # เวลาที่เหลือให้ใช้ได้
        remaining_budget_sec = MAX_RUNTIME_SEC - elapsed_total
        
        if remaining_budget_sec <= 0:
            print("⚠️ Time Limit Exceeded! Skipping Random Delay.")
            safe_max_delay_min = 0
        else:
            # แปลงวินาทีที่เหลือ เป็นนาที
            remaining_budget_min = remaining_budget_sec / 60
            
            # เลือกค่าที่น้อยกว่า ระหว่าง "Config เดิม" กับ "เวลาที่เหลือจริง"
            # เช่น Config ตั้งไว้ 90 นาที แต่เวลาเหลือแค่ 30 นาที -> ก็เอาแค่ 30 นาที
            safe_max_delay_min = min(context['max_wait_min'], remaining_budget_min)
            
            # กันพลาด: ถ้าเหลือน้อยมากๆ (ต่ำกว่า 1 นาที) ให้ข้าม
            if safe_max_delay_min < 1: safe_max_delay_min = 0

        # 3. เริ่ม Random Delay ด้วยค่าที่ปลอดภัย (Safe Delay)
        apply_random_delay(safe_max_delay_min)

        # 4. เตรียมเนื้อหา
        client, api_v1 = get_twitter_client()
        message = prepare_message(context['msg_index'], bot_data["messages"], hashtag_pool)
        
        bot_ui.print_preview_box(message)

        # 5. อัปโหลดรูป
        media_ids = []
        if context['upload_image'] and "images" in bot_data:
            media_ids = upload_images(api_v1, bot_data["images"])

        # 6. โพสต์
        post_tweet(client, message, media_ids)

    except Exception as e:
        print("\n" + "!"*50)
        print(f"❌ CRITICAL SYSTEM ERROR: {e}")
        print("!"*50)
    
    bot_ui.print_end()



