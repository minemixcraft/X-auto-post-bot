import time
from src.utils.helpers import get_thai_time, get_seconds_until_target

def wait_until_target_time(session, bot_ui, sleep_fn):
    target_hour = session['context']['target_hour']
    bot_ui.print_waiting_header()
    while True:
        now = get_thai_time()
        if now.hour >= target_hour:
            break 
        wait_seconds = get_seconds_until_target(now, target_hour)
        if wait_seconds > 0:
            sleep_fn(wait_seconds, start_msg="Timer Started", status_msg="Waiting...")
            break 
        else:
            time.sleep(30)
    bot_ui.print_closer()
