# ======================================================
# 🛠️ ไฟล์: bot_utils.py
# (ปรับปรุง: ใช้ Range Logic + ระบบรอเวลา Start)
# ======================================================

import os
import time
import random
import tweepy
from datetime import datetime, timezone, timedelta

def get_thai_time():
    """ดึงเวลาปัจจุบัน (Thailand Zone UTC+7)"""
    return datetime.now(timezone.utc) + timedelta(hours=7)

def get_zone_config(current_hour):
    """
    ตรวจสอบช่วงเวลาโดยใช้ Logic แบบ Range (<=) 
    เพื่อให้ครอบคลุมทุกช่วงเวลา ไม่ว่าจะรันตอนไหน
    """
    # 1. ช่วงเช้า (เที่ยงคืน ถึง 12:59) -> เป้าหมายเริ่มงาน 08:00
    if current_hour <= 12:
        return {
            "name": "Morning Round",
            "target_hour": 8,   # เริ่มงาน 8 โมง
            "msg_index": 0,
            "max_wait_random": 15 # สุ่มดีเลย์หลังเริ่มงานไม่เกิน 45 นาที
        }
    
    # 2. ช่วงบ่าย (13:00 ถึง 18:59) -> เป้าหมายเริ่มงาน 13:00
    elif current_hour <= 18:
        return {
            "name": "Afternoon Round",
            "target_hour": 13,  # เริ่มงาน 13 โมง
            "msg_index": 1,
            "max_wait_random": 90 # สุ่มดีเลย์หลังเริ่มงานไม่เกิน 90 นาที
        }
    
    # 3. ช่วงเย็น (19:00 ถึง 23:59) -> เป้าหมายเริ่มงาน 19:00
    else:
        return {
            "name": "Evening Round",
            "target_hour": 18,  # เริ่มงาน 19 โมง (1 ทุ่ม)
            "msg_index": 2,
            "max_wait_random": 30  # สุ่มดีเลย์หลังเริ่มงานไม่เกิน 15 นาที
        }

def wait_until_target_time(target_hour):
    """
    ฟังก์ชันสำหรับ 'รอ' ให้ถึงเวลาเริ่มงานจริงๆ
    - ถ้ามา 'ก่อน' -> นั่งรอ (Sleep)
    - ถ้ามา 'หลัง' -> ทำงานเลย
    """
    print(f"[Wait System] Checking time... Target is {target_hour}:00")
    
    while True:
        now = get_thai_time()
        
        # ถ้าชั่วโมงปัจจุบัน ยังน้อยกว่า เป้าหมาย (เช่น ตอนนี้ 7 โมง, เป้าหมาย 8 โมง)
        if now.hour < target_hour:
            minutes_left = (target_hour - now.hour) * 60 - now.minute
            print(f"\r⏳ Early Bird: Waiting for {target_hour}:00... (Current: {now.strftime('%H:%M:%S')})", end="")
            time.sleep(30) # เช็คทุกๆ 30 วินาที
        else:
            # ถึงเวลาแล้ว (หรือเลยมาแล้ว)
            print(f"\n✅ It's time! ({now.strftime('%H:%M:%S')}) Starting process...")
            break

def prepare_content_with_tags(msg_index, messages_list, hashtag_pool):
    """เตรียมข้อความ + สุ่มแฮชแท็ก"""
    if msg_index >= len(messages_list):
        msg_index = 0 # กัน Error ถ้า Index เกิน
        
    base_msg = messages_list[msg_index] + "\n\n"
    tags = list(set(hashtag_pool))
    random.shuffle(tags)
    
    final_msg = base_msg
    selected_tags = []
    
    for t in tags:
        if len(final_msg + t + " ") <= 280: 
            final_msg += t + " "
            selected_tags.append(t)
        else:
            break 
            
    return final_msg.strip(), selected_tags

def run_autopost_workflow(bot_name, bot_data, hashtag_pool):
    """
    🔥 ฟังก์ชันหลักสำหรับรันบอท (Logic ใหม่)
    """
    print("\n" + "="*50)
    print(f"🤖 {bot_name.upper()} X-BOT: AUTOPOST SYSTEM")
    print("="*50)

    # 1. เช็คเวลาและดึง Config ของโซนนั้นๆ
    start_time = get_thai_time()
    config = get_zone_config(start_time.hour)
    
    print(f"[Zone Detect] {config['name']} (Target: {config['target_hour']}:00)")

    # 2. เข้าสู่โหมดรอเวลา (ถ้ามาก่อนเวลา)
    wait_until_target_time(config['target_hour'])

    # 3. ตรวจสอบ API Keys
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        print("[Critical Error] API Keys not found in Environment Variables")
        return

    # 4. กลยุทธ์สุ่มเวลา (Random Delay) *หลัง* จากถึงเวลาเริ่มงานแล้ว
    # เพื่อไม่ให้บอทโพสต์เป๊ะเกินไปจนดูเหมือนหุ่นยนต์
    wait_sec = random.randint(60, config['max_wait_random'] * 60)
    print("-" * 50)
    print(f"[Strategy] Waiting random delay: {wait_sec // 60} min {wait_sec % 60} sec...")
    print("-" * 50)
    
    time.sleep(wait_sec)

    # 5. เริ่มการโพสต์
    try:
        # เชื่อมต่อ API
        client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api_v1 = tweepy.API(auth)
        
        # เตรียมเนื้อหา
        msg_to_post, _ = prepare_content_with_tags(
            config['msg_index'], 
            bot_data["messages"], 
            hashtag_pool
        )
        
        print("-" * 30)
        print("PREVIEW:\n" + msg_to_post)
        print("-" * 30)

        # อัปโหลดรูปภาพ (ถ้ามีและเป็นรอบเช้า)
        media_ids = []
        if config['msg_index'] == 0:  # โพสต์รูปเฉพาะรอบเช้า
            print("[Media] Checking images...")
            for img in bot_data["images"]:
                if os.path.exists(img):
                    try:
                        up = api_v1.media_upload(filename=img)
                        media_ids.append(up.media_id)
                        print(f"   - Uploaded: {img} [OK]")
                    except Exception as e:
                        print(f"   - Error uploading {img}: {e}")
                else:
                    print(f"   - Missing file: {img}")

        # ส่งทวีต
        print("[Sending] Posting tweet to X...")
        client.create_tweet(text=msg_to_post, media_ids=media_ids if media_ids else None)
        print(f"[Success] Posted successfully!")

    except Exception as e:
        print(f"[Error] Critical error: {e}")

    print("="*50 + "\n")
