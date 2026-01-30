# ======================================================
# 🛠️ ไฟล์: bot_utils.py
# (Refactored: Clean Code / Modular / Robust Logic)
# ======================================================

import os
import time
import random
import tweepy
from datetime import datetime, timezone, timedelta

# ======================================================
# 1. TIME & SCHEDULE MANAGEMENT (จัดการเวลา)
# ======================================================

def get_thai_time():
    """ดึงเวลาปัจจุบัน (Thailand Zone UTC+7)"""
    return datetime.now(timezone.utc) + timedelta(hours=7)

def get_schedule_context(current_hour):
    """
    ตรวจสอบและคืนค่า Config ตามช่วงเวลา
    (ปรับปรุง: รองรับการรันล่วงหน้า 2 ชั่วโมงได้จริง 100%)
    """
    if current_hour < 10:
        return {
            "name": "Morning Round",
            "msg_index": 0,
            "max_wait_min": 45,
            "target_hour": 8,
            "upload_image": True
        }
    elif current_hour < 15:
        return {
            "name": "Afternoon Round",
            "msg_index": 1,
            "max_wait_min": 60,
            "target_hour": 12, # แก้เป็น 12 ตามที่คุณต้องการ
            "upload_image": False
        }
    else:
        return {
            "name": "Evening Round",
            "msg_index": 2,
            "max_wait_min": 90,
            "target_hour": 17, # แก้เป็น 17 ตามที่คุณต้องการ
            "upload_image": False
        }

def wait_for_schedule_start(target_hour):
    """
    รอให้ถึงเวลาเริ่มงาน (Blocking Wait)
    - ถ้ามาก่อนเวลา: รอนับถอยหลัง
    - ถ้ามาหลังเวลา: ผ่านไปทำต่อทันที
    """
    print(f"[Wait System] Checking time... Target is {target_hour}:00")
    
    while True:
        now = get_thai_time()
        if now.hour < target_hour:
            print(f"\r⏳ Early Bird: Waiting for {target_hour}:00... (Current: {now.strftime('%H:%M:%S')})", end="")
            time.sleep(30) # เช็คทุก 30 วินาที
        else:
            print(f"\n✅ It's time! ({now.strftime('%H:%M:%S')}) Starting process...")
            break

def apply_random_delay(max_minutes):
    """สุ่มเวลาหน่วงหลังเริ่มงาน (Anti-Bot Detection)"""
    if max_minutes <= 0:
        return

    wait_sec = random.randint(60, max_minutes * 60)
    minutes = wait_sec // 60
    seconds = wait_sec % 60
    
    print("-" * 50)
    print(f"[Strategy] Random delay: {minutes} min {seconds} sec...")
    print("-" * 50)
    time.sleep(wait_sec)

# ======================================================
# 2. CONTENT PREPARATION (เตรียมเนื้อหา)
# ======================================================

def prepare_message(msg_index, messages_list, hashtag_pool):
    """ประกอบร่างข้อความและแฮชแท็ก"""
    # ป้องกัน Index Error
    if msg_index >= len(messages_list):
        msg_index = 0
        
    base_msg = messages_list[msg_index].strip() + "\n\n"
    
    # สุ่มแฮชแท็ก
    tags = list(set(hashtag_pool))
    random.shuffle(tags)
    
    final_msg = base_msg
    for t in tags:
        # เช็คความยาวไม่เกิน 280 (เผื่อที่ไว้นิดหน่อย)
        if len(final_msg + t + " ") <= 280: 
            final_msg += t + " "
        else:
            break 
            
    return final_msg.strip()

# ======================================================
# 3. TWITTER API INTERACTION (ติดต่อ Twitter)
# ======================================================

def get_twitter_client():
    """ดึง Environment Variables และเชื่อมต่อ API"""
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise ValueError("❌ Missing API Keys in Environment Variables")

    # Client (v2) สำหรับโพสต์
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    
    # API (v1.1) สำหรับอัปโหลดรูป
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    api_v1 = tweepy.API(auth)
    
    return client, api_v1

def upload_images(api_v1, image_paths):
    """อัปโหลดรูปภาพและคืนค่า Media IDs"""
    media_ids = []
    print("[Media] Processing images...")
    
    for img_path in image_paths:
        if os.path.exists(img_path):
            try:
                upload = api_v1.media_upload(filename=img_path)
                media_ids.append(upload.media_id)
                print(f"   - Uploaded: {img_path} [ID: {upload.media_id}]")
            except Exception as e:
                print(f"   - ⚠️ Error uploading {img_path}: {e}")
        else:
            print(f"   - ⚠️ File not found: {img_path}")
            
    return media_ids

def post_tweet(client, message, media_ids=None):
    """ส่งทวีตสุดท้ายไปยัง X"""
    print("[Sending] Posting tweet to X...")
    try:
        response = client.create_tweet(text=message, media_ids=media_ids)
        print(f"[Success] Tweet Sent! ID: {response.data['id']}")
        return True
    except Exception as e:
        print(f"[Error] Failed to tweet: {e}")
        return False

# ======================================================
# 4. MAIN ORCHESTRATOR (ผู้คุมวง)
# ======================================================

def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    """
    ฟังก์ชันหลัก: ควบคุมลำดับการทำงานทั้งหมด
    """
    print("\n" + "="*50)
    print(f"🤖 {bot_name.upper()} X-BOT STARTED")
    print("="*50)

    try:
        # Step 1: ตรวจสอบเวลาและบริบท
        start_time = get_thai_time()
        context = get_schedule_context(start_time.hour)
        print(f"[Context] {context['name']} (Target: {context['target_hour']}:00)")

        # Step 2: รอจนกว่าจะถึงเวลาเริ่มงาน (System Wait)
        wait_for_schedule_start(context['target_hour'])

        # Step 3: สุ่มเวลาหน่วง (Random Delay)
        apply_random_delay(context['max_wait_min'])

        # Step 4: เชื่อมต่อ API
        client, api_v1 = get_twitter_client()

        # Step 5: เตรียมเนื้อหา
        message = prepare_message(
            context['msg_index'], 
            bot_data["messages"], 
            hashtag_pool
        )
        print(f"\n📝 PREVIEW:\n{message}\n{'-'*30}")

        # Step 6: จัดการรูปภาพ (เฉพาะรอบที่กำหนด)
        media_ids = []
        if context['upload_image'] and "images" in bot_data:
            media_ids = upload_images(api_v1, bot_data["images"])

        # Step 7: โพสต์จริง
        post_tweet(client, message, media_ids)

    except Exception as e:
        print(f"\n❌ CRITICAL WORKFLOW ERROR: {e}")
    
    print("\n" + "="*50)
    print("✅ WORKFLOW COMPLETED")
    print("="*50 + "\n")

