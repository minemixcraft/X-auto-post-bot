import os
import time
import random
import tweepy
from datetime import datetime
from config.settings import SCHEDULE_CONFIG, SYSTEM_CONFIG, TWITTER_LIMITS
from src.utils.helpers import (
    get_thai_time, calculate_time_budget, calculate_safe_delay
)
from src.utils.tweet_analyzer import analyze_tweet_weight, calculate_x_char_weight
from src.utils.validator import prepare_tweet_content, filter_existing_images
from src.core.api import get_twitter_api
from src.core.scheduler import wait_until_target_time

def sleep_with_progress_bar(seconds, bot_ui, start_msg=None, status_msg="Waiting...", end_msg=None):
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

def upload_single_file(api_v1, filepath, bot_ui):
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

def perform_system_check(session, bot_ui):
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

def execute_safety_delay_strategy(session, bot_ui):
    elapsed_min, remaining_min = calculate_time_budget(session['workflow_start'], session['max_runtime_min'])
    config_delay = session['context']['max_wait_min']
    safe_delay = calculate_safe_delay(config_delay, remaining_min)

    bot_ui.print_execution_header()
    bot_ui.print_time_budget(session['max_runtime_min'], elapsed_min, remaining_min, config_delay, safe_delay)

    if safe_delay > 0:
        wait_sec = random.randint(60, int(safe_delay * 60))
        bot_ui.print_strategy_info(wait_sec // 60, wait_sec % 60)
        sleep_with_progress_bar(wait_sec, bot_ui, status_msg="Sleeping...", end_msg="Waking Up!")
    else:
        print("   ➤ Skipped Random Delay (Budget tight or Config 0)")
    bot_ui.print_closer()

def generate_and_preview_content(session, bot_ui, show_preview):
    ctx = session['context']
    message = prepare_tweet_content(
        ctx['msg_index'], 
        session['bot_data'].get("messages", []), 
        session['hashtag_pool']
    )
    if show_preview:
        weight_stats = analyze_tweet_weight(message)
        bot_ui.print_preview_box(message, weight_stats)
    return message

def handle_media_uploads(api_v1, session, bot_ui):
    ctx = session['context']
    bot_data = session['bot_data']
    bot_ui.print_upload_header()
    media_ids = []
    if ctx['upload_image'] and "images" in bot_data:
        valid_images = filter_existing_images(bot_data["images"])
        bot_ui.print_media_found(len(valid_images))
        for img in valid_images:
            mid = upload_single_file(api_v1, img, bot_ui)
            if mid: media_ids.append(mid)
    bot_ui.print_closer()
    return media_ids

def publish_tweet_to_x(client, message, media_ids, bot_ui):
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
        
    except tweepy.TweepyException as e:
        print("\n   ❌ [TWITTER API ERROR]")
        print(f"   ➤ Type  : {type(e)}")
        print(f"   ➤ Error : {repr(e)}")
        
        if hasattr(e, "response") and e.response is not None:
            print(f"   ➤ STATUS: {e.response.status_code}")
            print(f"   ➤ BODY  : {e.response.text}")
        raise 
        
    except Exception as e:
        print(f"\n   ❌ [UNEXPECTED ERROR]")
        print(f"   ➤ Error : {repr(e)}")
        raise
        
    bot_ui.print_closer()

def handle_critical_error(e):
    print("\n" + "!"*50)
    print(f"❌ CRITICAL SYSTEM ERROR: {e}")
    print("!"*50)

def run_autopost_workflow(bot_name, bot_data, hashtag_pool, bot_ui, show_preview):
    bot_ui.print_header(bot_name)
    try:
        session = initialize_bot_session(bot_data, hashtag_pool)
        perform_system_check(session, bot_ui)
        wait_until_target_time(session, bot_ui, lambda secs, **k: sleep_with_progress_bar(secs, bot_ui, **k))
        execute_safety_delay_strategy(session, bot_ui)
        client, api_v1 = get_twitter_api()
        message = generate_and_preview_content(session, bot_ui, show_preview)
        media_ids = handle_media_uploads(api_v1, session, bot_ui)
        publish_tweet_to_x(client, message, media_ids or None, bot_ui)
    except Exception as e:
        handle_critical_error(e)
    bot_ui.print_end()

def run_manual_workflow(bot_name, bot_data, hashtag_pool, bot_ui, show_preview):
    """Workflow สำหรับเทส (ข้ามการรอเวลา)"""
    bot_ui.print_header(bot_name)
    try:
        session = initialize_bot_session(bot_data, hashtag_pool)
        perform_system_check(session, bot_ui)
        client, api_v1 = get_twitter_api()
        message = generate_and_preview_content(session, bot_ui, show_preview)
        media_ids = handle_media_uploads(api_v1, session, bot_ui)
        publish_tweet_to_x(client, message, media_ids or None, bot_ui)
    except Exception as e:
        handle_critical_error(e)
    bot_ui.print_end()
