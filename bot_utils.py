# ======================================================
# 🛠️ ไฟล์: bot_utils.py
# (เก็บฟังก์ชันคำนวณ และ Workflow หลักของการโพสต์)
# ======================================================

import os
import time
import random
import tweepy
from datetime import datetime, timezone, timedelta

def get_thai_time():
    """ดึงเวลาปัจจุบัน (Thailand Zone UTC+7)"""
    return datetime.now(timezone.utc) + timedelta(hours=7)

def get_current_zone(thai_now):
    """คำนวณรอบการทำงาน (เผื่อเวลาดีเลย์ให้ 1 ชั่วโมง)"""
    h = thai_now.hour
    
    # รอบเช้า: ปกติ 08:xx (เผื่อดีเลย์เป็น 09:xx ได้)
    if h == 8 or h == 9: 
        return {"name": "Morning Round", "msg_index": 0, "max_wait_min": 45}
    
    # รอบกลางวัน: ปกติ 12:xx (เผื่อดีเลย์เป็น 13:xx ได้)
    elif h == 12 or h == 13:
        return {"name": "Afternoon Round", "msg_index": 1, "max_wait_min": 90}
    
    # รอบเย็น: ปกติ 17:xx (เผื่อดีเลย์เป็น 18:xx ได้)
    elif h == 17 or h == 18 or h == 20 or h == 19:
        return {"name": "Evening Round", "msg_index": 2, "max_wait_min": 5}
        
    return None

def prepare_content_with_tags(msg_index, messages_list, hashtag_pool):
    """เตรียมข้อความ + สุ่มแฮชแท็ก"""
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
    🔥 ฟังก์ชันหลักสำหรับรันบอททุกตัว (รวม Logic ไว้ที่นี่ที่เดียว)
    """
    print("\n" + "="*50)
    print(f"🤖 {bot_name.upper()} X-BOT: AUTOPOST SYSTEM")
    print("="*50)

    # 1. เช็คเวลาและโซน
    start_time = get_thai_time()
    print(f"[Time Check] Bot started at: {start_time.strftime('%H:%M:%S')}")

    zone = get_current_zone(start_time)
    if not zone:
        print(f"[Status] Outside schedule -> Exiting")
        return

    print(f"[Target] Current Zone: {zone['name']}")

    # 2. ตรวจสอบ API Keys
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        print("[Critical Error] API Keys not found in Environment Variables")
        return

    # 3. กลยุทธ์การรอเวลา (Random Delay)
    wait_sec = random.randint(60, zone['max_wait_min'] * 60)
    print("-" * 50)
    print(f"[Strategy] Waiting for {wait_sec // 60} min {wait_sec % 60} sec...")
    print("-" * 50)
    time.sleep(wait_sec)

    # 4. เริ่มการโพสต์
    try:
        # เชื่อมต่อ API
        client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api_v1 = tweepy.API(auth)
        
        # เตรียมเนื้อหา
        msg_to_post, _ = prepare_content_with_tags(
            zone['msg_index'], 
            bot_data["messages"], 
            hashtag_pool
        )
        
        print("-" * 30)
        print("PREVIEW:\n" + msg_to_post)
        print("-" * 30)

        # อัปโหลดรูปภาพ (ถ้ามีและเป็นรอบเช้า)
        media_ids = []
        if zone['msg_index'] == 0: 
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

