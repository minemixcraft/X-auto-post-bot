# ======================================================
# 🎨 ไฟล์: bot_ui.py (ASCII Art Version)
# (Compatible Interface with bot_ui_text.py)
# ======================================================

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
    if key in ASCII_ART:
        print(ASCII_ART[key].strip())

# ======================================================
# 1. CORE PRINTING FUNCTIONS
# ======================================================

def print_header(bot_name):
    print("\n" + "="*50)
    print_art("HEADER")
    print(f"          {bot_name.upper()}")
    print("="*50 + "\n")

def print_section(key):
    print("\n" + "-"*40)
    print_art(key)
    print("-"*40)

def print_closer():
    print("-" * 40)

def print_info(label, value):
    print(f"   ➤ {label:<13} : {value}")

def print_error(message):
    print(f"   ❌ {message}")

# ======================================================
# 2. SPECIFIC SECTIONS
# ======================================================

def print_system_check(context_name, target_time, current_date, current_time, upload_image, msg_count, tag_count, max_delay):
    print_section("SYSTEM_CHECK")
    print_info("Context", context_name)
    print_info("Target Time", target_time)
    print_info("Current Date", current_date)
    print_info("Current Time", current_time)
    print_info("Has Image?", 'Yes' if upload_image else 'No')
    print("")
    print_info("Msg Loaded", f"{msg_count} items")
    print_info("Tag Pool", f"{tag_count} tags")
    print_info("Max Delay", f"{max_delay} mins")
    print_closer()

def print_waiting_header():
    print_section("WAITING")

def print_waiting_bar(percent, remaining_seconds, is_finished=False, custom_status=None):
    bar_length = 25
    filled_length = int(bar_length * percent // 100)
    if is_finished:
        pass
    else:
        bar_char = '▒'
        status_text = custom_status if custom_status else "Waiting..."
        time_str = format_time_str(remaining_seconds)
        bar = bar_char * filled_length + '░' * (bar_length - filled_length)
        print(f"   {bar} {percent}% | ETA: {time_str} | {status_text}")

def print_execution_header():
    print_section("EXECUTION")

def print_time_budget(limit_min, elapsed_min, remaining_min, config_delay, safe_delay):
    print("   [TIME BUDGET ANALYSIS]")
    print(f"   ➤ Limit: {limit_min}m | Used: {elapsed_min:.1f}m | Left: {remaining_min:.1f}m")
    print(f"   ➤ Config: {config_delay}m -> Safe: {int(safe_delay)}m")
    print("   " + "-"*30)

def print_strategy_info(wait_minutes, wait_seconds):
    print_info("Strategy", f"Random Delay ({wait_minutes}m {wait_seconds}s)")
    print("   ... (Sleeping) ...")

def print_preview_box(message):
    lines = message.split('\n')
    max_len = 0
    for line in lines:
        if len(line) > max_len: max_len = len(line)
    box_width = max(max_len + 4, 30)
    
    print_section("PREVIEW")
    print("┌" + "─" * box_width + "┐")
    for line in lines:
        print(f"│ {line:<{box_width-1}}│") 
    print("└" + "─" * box_width + "┘")

def print_upload_header():
    print_section("UPLOADING")

def print_media_found(count):
    print(f"   ➤ Media Found   : {count} Images")

def print_upload_item(filename, media_id):
    print(f"   ✔ Uploaded      : {filename} [ID: {str(media_id)[:3]}...]")

def print_upload_error(filename, error):
    print(f"   ❌ Error {filename} : {error}")

def print_pose_header():
    # ใช้ Art ของ EXECUTION เพราะไม่มี POSE
    print_section("EXECUTION") 

def print_post_success(tweet_id):
    print("\n       ✅ [TWEET POSTED SUCCESSFULLY]")
    print(f"   ➤ Tweet ID      : {tweet_id}")

def print_end():
    print_section("COMPLETED")
    print("✅ WORKFLOW COMPLETED")
    print("=" * 52 + "\n")
