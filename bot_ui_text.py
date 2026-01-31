# ======================================================
# 🎨 ไฟล์: bot_ui_text.py
# (Custom UI: d[o_0]b Style with Steps [1/4] & Budget Analysis)
# ======================================================

def format_time_str(total_seconds):
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

# ======================================================
# 1. CORE PRINTING FUNCTIONS
# ======================================================

def print_header(bot_name):
    """แสดง Header หน้า Robot d[o_0]b"""
    width = 52
    title = f"d[o_0]b {bot_name.upper()} X-BOT"
    print("\n" + "╔" + "═"*width + "╗")
    print(f"║ {title:^{width}} ║")
    print("╚" + "═"*width + "╝")

def print_section_header(title):
    """แสดงหัวข้อพร้อมเส้นคู่"""
    print(f"\n{title}")
    print("=" * 52)

def print_closer():
    """เส้นปิดท้าย Section"""
    print("=" * 52)

def print_info(label, value):
    print(f"   ➤ {label:<13} : {value}")

def print_error(message):
    print(f"   ❌ {message}")

# ======================================================
# 2. SPECIFIC SECTIONS
# ======================================================

def print_system_check(context_name, target_time, current_date, current_time, upload_image, msg_count, tag_count, max_delay):
    print_section_header("⚙️ [SYSTEM CHECK]")
    print_info("Time Zone", "Asia/Bangkok (UTC+7)")
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

# --- STEP 1: WAITING ---
def print_waiting_header():
    print_section_header("⏱︎ [WAITING PROCESS]  [1/4]")

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

# --- STEP 2: EXECUTION ---
def print_execution_header():
    print_section_header("  [EXECUTION START] [2/4]")

def print_time_budget(limit_min, elapsed_min, remaining_min, config_delay, safe_delay):
    """แสดงตารางวิเคราะห์เวลา (Time Budget Analysis)"""
    # ไม่ต้องมี Header ใหญ่ซ้ำ เพราะเรียกต่อจาก execution_header
    print(" 📊 [TIME BUDGET ANALYSIS]")
    print(f"   ➤ Total Runtime   : {limit_min} mins (Safety Limit)")
    print(f"   ➤ Time Elapsed    : {elapsed_min:.1f} mins (Used in Wait)")
    print(f"   ➤ Remaining       : {remaining_min:.1f} mins")
    print(f"   ➤ Config Delay    : {config_delay} mins")
    
    if safe_delay < config_delay:
        print(f"   ➤ Safe Delay      : {int(safe_delay)} mins ⚠️ (Adjusted)")
    else:
        print(f"   ➤ Safe Delay      : {int(safe_delay)} mins (OK)")
    
    print(" " + "-"*50)

def print_strategy_info(wait_minutes, wait_seconds):
    print(f"   ➤ Strategy        : Random Delay ({wait_minutes}m {wait_seconds}s)")
    print("   ... (Sleeping) ...")

# --- PREVIEW ---
def print_preview_box(message):
    lines = message.split('\n')
    max_len = 0
    for line in lines:
        if len(line) > max_len: max_len = len(line)
    box_width = max(max_len + 4, 30)
    
    print_section_header(" 🗟 [TWEET PREVIEW]")
    print("┌" + "─" * box_width + "┐")
    for line in lines:
        print(f"│ {line:<{box_width-1}}│") 
    print("└" + "─" * box_width + "┘")

# --- STEP 3: UPLOADING ---
def print_upload_header():
    print_section_header("  [UPLOADING] [3/4]")

def print_media_found(count):
    print(f"   ➤ Media Found   : {count} Images")

def print_upload_item(filename, media_id):
    print(f"   ✔ Uploaded      : {filename} [ID: {str(media_id)[:3]}...]")

def print_upload_error(filename, error):
    print(f"   ❌ Error {filename} : {error}")

# --- STEP 4: POSE ---
def print_pose_header():
    print_section_header("  [POSE]       [4/4]")

def print_post_success(tweet_id):
    print("\n       ✅ [TWEET POSTED SUCCESSFULLY]")
    print(f"   ➤ Tweet ID      : {tweet_id}")

# --- END ---
def print_end():
    print_section_header("  [END]")
    print("✅ WORKFLOW COMPLETED")
    print("=" * 52 + "\n")
