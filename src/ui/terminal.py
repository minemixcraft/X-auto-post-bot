import os
from config.settings import UI_CONFIG

ACTIVE_STYLE = UI_CONFIG.get("PROGRESS_STYLE", "VERTICAL")
UI_STYLE = UI_CONFIG.get("MODULE_NAME", "text")  # "ascii" or "text"

BAR_STYLES = {
    "BLOCK":    {"fill": "█", "empty": "░"},
    "SHADE":    {"fill": "▒", "empty": "░"},
    "RECT":     {"fill": "▰", "empty": "▱"},
    "CIRCLE":   {"fill": "o", "empty": "."},
    "VERTICAL": {"fill": "▮", "empty": "▯"},
    "SQUARE":   {"fill": "■", "empty": "□"},
}

ASCII_ART = {
    "HEADER": """
░█▀▄░█▀█░▀█▀░░░░
░█▀▄░█░█░░█░░░▀░
░▀▀░░▀▀▀░░▀░░░▀░
    """,
    "SYSTEM_CHECK": """
░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█▄█░░░█▀▀░█░█░█▀▀░█▀▀░█░█
░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█░░░█░░░█▀█░█▀▀░█░░░█▀▄
░▀▀▀░░▀░░▀▀▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀
    """,
    "WAITING": """
░█░█░█▀█░▀█▀░▀█▀░▀█▀░█▀█░█▀▀
░█▄█░█▀█░░█░░░█░░░█░░█░█░█░█
░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀
    """,
    "EXECUTION": """
░█▀▀░█░█░█▀▀░█▀▀░█░█░▀█▀░▀█▀░█▀█░█▀█
░█▀▀░▄▀▄░█▀▀░█░░░█░█░░█░░░█░░█░█░█░█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀
    """,
    "PREVIEW": """
░█▀█░█▀▄░█▀▀░█░█░▀█▀░█▀▀░█░█
░█▀▀░█▀▄░█▀▀░▀▄▀░░█░░█▀▀░█▄█
░▀░░░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀
    """,
    "UPLOADING": """
░█░█░█▀█░█░░░█▀█░█▀█░█▀▄░▀█▀░█▀█░█▀▀
░█░█░█▀▀░█░░░█░█░█▀█░█░█░░█░░█░█░█░█
░▀▀▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀
    """,
    "COMPLETED": """
░█▀▀░█▀█░█▄█░█▀█░█░░░█▀▀░▀█▀░█▀▀░█▀▄
░█░░░█░█░█░█░█▀▀░█░░░█▀▀░░█░░█▀▀░█░█
░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀░
    """
}

def format_time_str(total_seconds):
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def print_art(key):
    if UI_STYLE == "ascii" and key in ASCII_ART:
        print(ASCII_ART[key].strip())

def print_header(bot_name):
    if UI_STYLE == "ascii":
        print("\n" + "="*50)
        print_art("HEADER")
        print(f"          {bot_name.upper()}")
        print("="*50 + "\n")
    else:
        width = 52
        title = f"d[o_0]b {bot_name.upper()} X-BOT"
        print("\n" + "╔" + "═"*width + "╗")
        print(f"║ {title:^{width}} ║")
        print("╚" + "═"*width + "╝")

def print_section_header(title, key=None):
    if UI_STYLE == "ascii" and key:
        print("\n" + "-"*40)
        print_art(key)
        print("-"*40)
    else:
        print(f"\n{title}")
        print("=" * 52)

def print_closer():
    if UI_STYLE == "ascii":
        print("-" * 40)
    else:
        print("=" * 52)

def print_info(label, value):
    print(f"   ➤ {label:<13} : {value}")

def print_error(message):
    print(f"   ❌ {message}")

def print_system_check(context_name, target_time, current_date, current_time, upload_image, msg_count, tag_count, max_delay):
    print_section_header("⚙️ [SYSTEM CHECK]", "SYSTEM_CHECK")
    if UI_STYLE == "text":
        print_info("Time Zone", "Asia/Bangkok (UTC+7)")
        print_info("Current Date", current_date)
        print_info("Current Time", current_time)
        print(" ") 
        print_info("Context", context_name)
        print_info("Target Time", target_time)
        print(" ") 
        print_info("Image", 'Yes' if upload_image else 'No')
    else:
        print_info("Context", context_name)
        print_info("Target Time", target_time)
        print_info("Current Date", current_date)
        print_info("Current Time", current_time)
        print("")
    print_info("Msg Loaded", f"{msg_count} items")
    print_info("Tag Pool", f"{tag_count} tags")
    print_info("Max Delay", f"{max_delay} mins")
    print_closer()

def print_waiting_header():
    print_section_header("⏱︎ [WAITING PROCESS]  [1/4]", "WAITING")

def print_waiting_bar(percent, remaining_seconds, is_finished=False, custom_status=None):
    default_bar = "RECT" if UI_STYLE == "ascii" else "SHADE"
    style = BAR_STYLES.get(ACTIVE_STYLE, BAR_STYLES[default_bar])
    fill_char = style["fill"]
    empty_char = style["empty"]
    bar_length = 25
    
    if is_finished:
        percent = 100
        remaining_seconds = 0
        status_text = custom_status if custom_status else "Target Reached!"
    else:
        status_text = custom_status if custom_status else "Waiting..."
    
    filled_length = int(bar_length * percent // 100)
    bar = fill_char * filled_length + empty_char * (bar_length - filled_length)
    time_str = format_time_str(remaining_seconds)
    
    print(f"   {bar} {percent}% | ETA: {time_str} | {status_text}")

def print_execution_header():
    print_section_header("  [EXECUTION START] [2/4]", "EXECUTION")

def print_time_budget(limit_min, elapsed_min, remaining_min, config_delay, safe_delay):
    if UI_STYLE == "ascii":
        print("   [TIME BUDGET ANALYSIS]")
        print(f"   ➤ Limit: {limit_min}m | Used: {elapsed_min:.1f}m | Left: {remaining_min:.1f}m")
        if safe_delay < config_delay:
            print(f"   ➤ Config: {config_delay}m -> Safe: {int(safe_delay)}m ⚠️ (Adjusted)")
        else:
            print(f"   ➤ Config: {config_delay}m -> Safe: {int(safe_delay)}m (OK)")
        print("   " + "-"*30)
    else:
        print(" 📊 [TIME BUDGET ANALYSIS]")
        print(f"   ➤ Total Runtime   : {limit_min} mins")
        print(f"   ➤ Time Elapsed    : {elapsed_min:.1f} mins")
        print(f"   ➤ Remaining       : {remaining_min:.1f} mins")
        
        if safe_delay < config_delay:
            print(f"   ➤ Config: {config_delay}m -> Safe: {int(safe_delay)}m ⚠️ (Adjusted)")
        else:
            print(f"   ➤ Config: {config_delay}m -> Safe: {int(safe_delay)}m (OK)")
        
        print(" " + "-"*50)

def print_strategy_info(wait_minutes, wait_seconds):
    if UI_STYLE == "ascii":
        print_info("Strategy", f"Random Delay ({wait_minutes}m {wait_seconds}s)")
    else:
        print(f"   ➤ Strategy        : Random Delay ({wait_minutes}m {wait_seconds}s)")
    print("   ... (Sleeping) ...")

def print_preview_box(message, stats=None):
    lines = message.split('\n')
    max_len = 0
    for line in lines:
        if len(line) > max_len: max_len = len(line)
    box_width = max(max_len + 4, 30)
    
    print_section_header(" 🗟 [TWEET PREVIEW]", "PREVIEW")
    print("┌" + "─" * box_width + "┐")
    for line in lines:
        print(f"│ {line:<{box_width-1}}│") 
    print("└" + "─" * box_width + "┘")

    if stats:
        if UI_STYLE == "ascii":
            print(f"\n   📊 Weight: {stats['total_weight']}/280")
        else:
            print(f"\n   📊 Weight Analysis ({stats['total_weight']}/280)")
            print(f"   --------------------------------------------------")
            print(f"   ➤ Text (TH/EN)    : {stats['text_count']:<3} chars = {stats['text_weight']:<3} units")
            print(f"   ➤ Emoji/Special   : {stats['emoji_count']:<3} chars = {stats['emoji_weight']:<3} units")
            print(f"   ➤ Space/Newline   : {stats['space_count']:<3} chars = {stats['space_weight']:<3} units")
            if stats['link_count'] > 0:
                print(f"   ➤ Links (URL)     : {stats['link_count']:<3} links = {stats['link_weight']:<3} units")
            print(f"   --------------------------------------------------")

def print_upload_header():
    print_section_header("  [UPLOADING] [3/4]", "UPLOADING")

def print_media_found(count):
    print(f"   ➤ Media Found   : {count} Images")

def print_upload_item(filename, media_id):
    print(f"   ✔ Uploaded      : {filename} [ID: {str(media_id)[:3]}...]")

def print_upload_error(filename, error):
    print(f"   ❌ Error {filename} : {error}")

def print_pose_header():
    print_section_header("  [POSE]       [4/4]", "EXECUTION")

def print_post_success(info):
    if UI_STYLE == "ascii":
        print("\n       ✅ [TWEET POSTED SUCCESSFULLY]")
        print(f"   ➤ Tweet ID      : {info['id']}")
        print(f"   ➤ Timestamp     : {info['timestamp']}")
        print(f"   ➤ Final Weight  : {info['weight']}/280")
    else:
        print("\n       ✅ [TWEET POSTED SUCCESSFULLY]")
        print(f"   ➤ Tweet ID      : {info['id']}")
        print(f"   ➤ Timestamp     : {info['timestamp']}")
        print(f"   ➤ Tweet URL     : {info['url']}")
        print(f"   ----------------------------------")
        print(f"   ➤ Media Uploaded: {info['media_count']} files")
        print(f"   ➤ Final Weight  : {info['weight']}/280 units")

def print_end():
    print_section_header("  [END]", "COMPLETED")
    print("✅ WORKFLOW COMPLETED")
    print("=" * 52 + "\n")
