import time
import random
from datetime import datetime, timezone, timedelta
from config.settings import SYSTEM_CONFIG

def get_thai_time():
    """คืนค่าเวลาปัจจุบัน (ตาม Config Timezone)"""
    offset = SYSTEM_CONFIG.get("TIMEZONE_HOURS", 7)
    return datetime.now(timezone(timedelta(hours=offset)))

def get_seconds_until_target(now, target_hour):
    target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    return (target_time - now).total_seconds()

def calculate_time_budget(start_time, max_runtime_min):
    elapsed_sec = time.time() - start_time
    remaining_sec = (max_runtime_min * 60) - elapsed_sec
    return elapsed_sec / 60, remaining_sec / 60

def calculate_safe_delay(config_delay_min, remaining_min):
    if remaining_min <= 0: return 0
    safe_delay = min(config_delay_min, remaining_min)
    return safe_delay if safe_delay >= 1 else 0
