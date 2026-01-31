import os
import time
import random
import tweepy
from datetime import datetime, timezone, timedelta

# 🔥 IMPORT UI MODULE
import bot_ui_text as bot_ui 
# import bot_ui as bot_ui 

# ======================================================
# 1. PURE LOGIC & CALCULATIONS (คำนวณอย่างเดียว ไม่มี Side Effect)
# ======================================================

def get_thai_time():
    """คืนค่าเวลาปัจจุบันในไทย"""
    return datetime.now(timezone.utc) + timedelta(hours=7)

def get_seconds_until_target(now, target_hour):
    """คำนวณวินาทีที่ต้องรอจนถึงเป้าหมาย"""
    target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    return (target_time - now).total_seconds()

def get_schedule_context(current_hour):
    """คืนค่า Config ของรอบเวลาตามชั่วโมงปัจจุบัน"""
    if current_hour < 10:
        return {"name": "Morning Round", "msg_index": 0, "max_wait_min": 45, "target_hour": 8, "upload_image": True}
    elif current_hour < 15:
        return {"name": "Afternoon Round", "msg_index": 1, "max_wait_min": 60, "target_hour": 12, "upload_image": False}
    else:
        return {"name": "Evening Round", "msg_index": 2, "max_wait_min": 90, "target_hour": 17, "upload_image": False}

def calculate_time_budget(start_time, max_runtime_min):
    """คำนวณเวลาที่ใช้ไปและเวลาที่เหลือ (Time Budget)"""
    elapsed_sec = time.time() - start_time
    remaining_sec = (max_runtime_min * 60) - elapsed_sec
    
    elapsed_min = elapsed_sec / 60
    remaining_min = remaining_sec / 60
    
    return elapsed_min, remaining_min

def calculate_safe_delay(config_delay_min, remaining_min):
    """คำนวณเวลา Random Delay ที่ปลอดภัย (ไม่เกินเวลาที่เหลือ)"""
    if remaining_min <= 0:
        return 0
    
    # เลือกค่าที่น้อยกว่า ระหว่าง Config กับ เวลาที่เหลือ
    safe_delay = min(config_delay_min, remaining_min)
    
    # ถ้าเหลือน้อยกว่า 1 นาที ให้ตัดเป็น 0 ไปเลยเพื่อความชัวร์
    return safe_delay if safe_delay >= 1 else 0

def prepare_tweet_content(msg_index, messages_list, hashtag_pool):
    """เตรียมข้อความและ Hashtag"""
    if not messages_list: return ""
    if msg_index >= len(messages_list): msg_index = 0
    
    base_msg = messages_list[msg_index].strip() + "\n\n"
    tags = list(set(hashtag_pool))
    random.shuffle(tags)
    
    final_msg = base_msg
    for t in tags:
        if len(final_msg + t + " ") <= 280:
            final_msg += t + " "
        else:
            break
            
    return final_msg.strip()

def filter_existing_images(image_paths):
    """กรองเฉพาะไฟล์รูปที่มีอยู่จริง"""
    if not image_paths: return []
    return [img for img in image_paths if os.path.exists(img)]

# ======================================================
# 2. LOW-LEVEL ACTIONS (ทำงานย่อยๆ 1 อย่าง)
# ======================================================

def get_twitter_api():
    """เชื่อมต่อ API"""
    keys = [os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"), os.getenv("X_ACCESS_TOKEN"), os.getenv("X_ACCESS_TOKEN_SECRET")]
    if not all(keys): raise ValueError("Missing API Keys")
    
    client = tweepy.Client(consumer_key=keys[0], consumer_secret=keys[1], access_token=keys[2], access_token_secret=keys[3])
    auth = tweepy.OAuth1UserHandler(keys[0], keys[1], keys[2], keys[3])
    api_v1 = tweepy.API(auth)
    return client, api_v1

def sleep_with_progress_bar(seconds, start_msg=None, status_msg="Waiting...", end_msg=None):
    """ฟังก์ชันหลับพร้อมแสดง Progress Bar (ใช้ซ้ำได้ทั้ง Wait และ Delay)"""
    if seconds <= 0: return

    effective_wait = max(0, seconds - 60) # Buffer 60 วิ
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
    """อัปโหลดไฟล์เดียว และคืนค่า Media ID"""
    try:
        upload = api_v1.media_upload(filename=filepath)
        bot_ui.print_upload_item(os.path.basename(filepath), upload.media_id)
        return upload.media_id
    except Exception as e:
        bot_ui.print_upload_error(filepath, e)
        return None

# ======================================================
# 3. HIGH-LEVEL TASKS (รวม Action มาทำงานเป็น Step)
# ======================================================

def process_system_check(context, start_time, bot_data, hashtag_pool):
    """[STEP 0] แสดงผลตรวจสอบระบบ"""
    bot_ui.print_system_check(
        context_name=context['name'], 
        target_time=f"{context['target_hour']}:00",
        current_date=start_time.strftime("%Y-%m-%d"),
        current_time=start_time.strftime("%H:%M:%S"),
        upload_image=context['upload_image'],
        msg_count=len(bot_data.get('messages', [])),
        tag_count=len(hashtag_pool),
        max_delay=context['max_wait_min']
    )

def process_waiting_for_target(target_hour):
    """[STEP 1] กระบวนการรอเวลาเป้าหมาย"""
    bot_ui.print_waiting_header()
    
    start_wait_time = time.time()
    
    while True:
        now = get_thai_time()
        if now.hour >= target_hour:
            break 
        
        wait_seconds = get_seconds_until_target(now, target_hour)
        if wait_seconds > 0:
            sleep_with_progress_bar(wait_seconds, start_msg="Timer Started", status_msg="Waiting...")
            break 
        else:
            time.sleep(30)
            
    bot_ui.print_closer()
    # คืนค่าเวลาที่ใช้รอไปจริง (วินาที)
    return time.time() - start_wait_time

def process_random_delay(max_wait_min):
    """[STEP 2] กระบวนการสุ่มเวลาหน่วง (Random Delay)"""
    bot_ui.print_execution_header() # ปริ้นหัวข้อก่อน (อาจจะปริ้น Budget ตามมาทีหลังใน Main)
    
    # หมายเหตุ: ใน Main เราจะปริ้น Budget ก่อน แล้วค่อยเรียกฟังก์ชันนี้เพื่อ sleep
    if max_wait_min > 0:
        wait_sec = random.randint(60, int(max_wait_min * 60))
        bot_ui.print_strategy_info(wait_sec // 60, wait_sec % 60)
        
        sleep_with_progress_bar(
            wait_sec, 
            status_msg="Sleeping...", 
            end_msg="Waking Up!"
        )
    else:
        print("   ➤ Strategy        : No Delay (Skipped)")
        
    bot_ui.print_closer()

def process_image_uploads(api_v1, image_paths):
    """[STEP 3] กระบวนการอัปโหลดรูปภาพทั้งหมด"""
    bot_ui.print_upload_header()
    
    valid_images = filter_existing_images(image_paths)
    bot_ui.print_media_found(len(valid_images))
    
    media_ids = []
    for img_path in valid_images:
        mid = upload_single_file(api_v1, img_path)
        if mid:
            media_ids.append(mid)
            
    bot_ui.print_closer()
    return media_ids

def process_posting(client, message, media_ids):
    """[STEP 4] กระบวนการโพสต์ทวีต"""
    bot_ui.print_pose_header()
    
    try:
        response = client.create_tweet(text=message, media_ids=media_ids)
        
        # 🔥 ดึงเวลาปัจจุบัน (ไทย) มาแสดงผล
        post_time = get_thai_time().strftime("%Y-%m-%d %H:%M:%S")
        
        # ส่ง tweet_id และ post_time ไปให้ UI
        bot_ui.print_post_success(response.data['id'], post_time)
        
    except Exception as e:
        print(f"   ❌ Failed to tweet: {e}")
        
    bot_ui.print_closer()
# ======================================================
# 3. HIGH-LEVEL TASKS (SRP Wrappers)
# ======================================================

def initialize_bot_session(bot_data, hashtag_pool):
    """รวบรวมตัวแปรที่จำเป็นต้องใช้ตลอด Session ไว้ใน Dictionary เดียว"""
    start_time = get_thai_time()
    context = get_schedule_context(start_time.hour)
    
    return {
        "start_time": start_time,
        "workflow_start": time.time(),
        "max_runtime_min": 110, # GitHub Limit Safety
        "context": context,
        "bot_data": bot_data,
        "hashtag_pool": hashtag_pool
    }

def perform_system_check(session):
    """แสดงผล System Check"""
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
    """รอจนกว่าจะถึงเวลาเป้าหมาย"""
    # เรียกใช้ process_waiting_for_target เดิมที่มีอยู่แล้ว
    process_waiting_for_target(session['context']['target_hour'])

def execute_safety_delay_strategy(session):
    """
    [Core Logic] คำนวณ Time Budget และสั่ง Sleep
    รวมการคำนวณ + การแสดงผล Header + การ Sleep ไว้ที่เดียว
    """
    # 1. คำนวณเวลา
    elapsed_min, remaining_min = calculate_time_budget(
        session['workflow_start'], 
        session['max_runtime_min']
    )
    
    # 2. หา Safe Delay
    config_delay = session['context']['max_wait_min']
    safe_delay = calculate_safe_delay(config_delay, remaining_min)

    # 3. แสดงผลตารางวิเคราะห์
    bot_ui.print_execution_header()
    bot_ui.print_time_budget(
        session['max_runtime_min'], 
        elapsed_min, 
        remaining_min, 
        config_delay, 
        safe_delay
    )

    # 4. สั่งนอนหลับ (ใช้ process_random_delay ที่มีอยู่แล้ว)
    if safe_delay > 0:
        # ใช้ Logic สุ่มเวลาจาก process_random_delay เดิม
        # แต่เราส่ง safe_delay ที่คำนวณแล้วเข้าไป
        wait_sec = random.randint(60, int(safe_delay * 60))
        bot_ui.print_strategy_info(wait_sec // 60, wait_sec % 60)
        sleep_with_progress_bar(wait_sec, status_msg="Sleeping...", end_msg="Waking Up!")
    else:
        print("   ➤ Skipped Random Delay (Budget tight or Config 0)")
    
    bot_ui.print_closer()

def connect_twitter_services():
    """เชื่อมต่อ API"""
    return get_twitter_api()

def generate_and_preview_content(session):
    """เตรียมข้อความและแสดง Preview"""
    ctx = session['context']
    message = prepare_tweet_content(
        ctx['msg_index'], 
        session['bot_data'].get("messages", []), 
        session['hashtag_pool']
    )
    bot_ui.print_preview_box(message)
    return message

def handle_media_uploads(api_v1, session):
    """จัดการอัปโหลดรูป (เช็คเงื่อนไขให้เอง)"""
    ctx = session['context']
    bot_data = session['bot_data']
    
    media_ids = []
    if ctx['upload_image'] and "images" in bot_data:
        media_ids = process_image_uploads(api_v1, bot_data["images"])
    
    return media_ids

def publish_tweet_to_x(client, message, media_ids):
    """โพสต์ทวีต"""
    process_posting(client, message, media_ids or None)

def handle_critical_error(e):
    """จัดการ Error"""
    print("\n" + "!"*50)
    print(f"❌ CRITICAL SYSTEM ERROR: {e}")
    print("!"*50)
# ======================================================
# 4. ORCHESTRATOR (MAIN WORKFLOW) - SRP STYLE
# ======================================================

def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    bot_ui.print_header(bot_name)

    try:
        # 1. เริ่มต้นระบบและโหลด Config
        # (รวม get_thai_time, get_context, ตั้งค่า Limit ไว้ในนี้)
        session = initialize_bot_session(bot_data, hashtag_pool)

        # 2. แสดงสถานะระบบ [System Check]
        perform_system_check(session)

        # 3. รอเวลาเป้าหมาย [Step 1]
        wait_until_target_time(session)

        # 4. คำนวณและหน่วงเวลาเพื่อความปลอดภัย [Step 2]
        # (ซ่อน Logic คำนวณ Budget และการสุ่มเวลาไว้ในนี้ทั้งหมด)
        # execute_safety_delay_strategy(session)

        # 5. เชื่อมต่อ Twitter API
        client, api_v1 = connect_twitter_services()

        # 6. เตรียมข้อความและแสดงตัวอย่าง
        message = generate_and_preview_content(session)

        # 7. จัดการอัปโหลดรูปภาพ (ถ้ามี) [Step 3]
        media_ids = handle_media_uploads(api_v1, session)

        # 8. โพสต์ทวีตจริง [Step 4]
        publish_tweet_to_x(client, message, media_ids)

    except Exception as e:
        handle_critical_error(e)
    
    bot_ui.print_end()



