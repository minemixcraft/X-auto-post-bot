# ======================================================
# 🎨 ไฟล์: bot_ui.py (ASCII Art Mode)
# (โครงสร้างเหมือน bot_ui_text.py เป๊ะ สลับใช้ได้เลย)
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
░█▀▀░█▀█░█▀▄
░█▀▀░█░█░█░█
░▀▀▀░▀░▀░▀▀░
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
# 1. CORE PRINTING FUNCTIONS (Standardized)
# ======================================================

def print_header(bot_name):
    print("\n" + "="*50)
    print_art("HEADER")
    print(f"          {bot_name.upper()}")
    print("="*50 + "\n")

def print_section_header(title):
    """
    รับ Title จาก bot_utils (เช่น '📌 [SYSTEM CHECK]')
    แล้วแปลงเป็น ASCII ART ที่ตรงกัน
    """
    # Map Keyword จาก Title ให้ตรงกับ Key ใน Dictionary
    upper_title = title.upper()
    art_key = None

    if "SYSTEM" in upper_title: art_key = "SYSTEM_CHECK"
    elif "WAITING" in upper_title: art_key = "WAITING"
    elif "EXECUTION" in upper_title: art_key = "EXECUTION"
    elif "PREVIEW" in upper_title: art_key = "PREVIEW"
    elif "UPLOADING" in upper_title: art_key = "UPLOADING"
    elif "POSE" in upper_title: art_key = "EXECUTION" # ใช้รูปเดียวกับ Execution
    elif "END" in upper_title: art_key = "COMPLETED"

    print("\n" + "-"*40)
    if art_key:
        print_art(art_key)
    else:
        # กรณีหา Art ไม่เจอ ให้ปริ้น Text ธรรมดา
        print(f" {title}")
    print("-"*40)

def print_closer():
    """ปิด Section ด้วยเส้นบางๆ"""
    print("-" * 40)

def print_info(label, value):
    print(f"   ➤ {label:<13} : {value}")

def print_error(message):
    print(f"   ❌ {message}")

# ======================================================
# 2. SPECIFIC SECTIONS (Interface Match)
# ======================================================

def print_system_check(context_name, target_time, upload_image):
    print_section_header("SYSTEM_CHECK")
    print_info("Context", context_name)
    print_info("Target Time", target_time)
    print_info("Has Image?", 'Yes' if upload_image else 'No')
    print_closer()

def print_waiting_bar(percent, remaining_seconds, is_finished=False, custom_status=None):
    bar_length = 25
    filled_length = int(bar_length * percent // 100)
    
    if is_finished:
        bar_char = '█'
        status_text = custom_status if custom_status else "READY TO START!"
    else:
        bar_char = '▒'
        status_text = custom_status if custom_status else "Waiting..."

    bar = bar_char * filled_length + '░' * (bar_length - filled_length)
    time_str = format_time_str(remaining_seconds)
    
    print(f"   {bar} {percent}% | ETA: {time_str} | {status_text}")

def print_preview_box(message):
    """
    ใช้ Logic Dynamic Width เหมือน Text Version 
    แต่มีหัวข้อเป็น ASCII Art
    """
    lines = message.split('\n')
    
    # คำนวณความกว้างกรอบ
    max_len = 0
    for line in lines:
        if len(line) > max_len: max_len = len(line)
    box_width = max(max_len + 4, 30)
    
    print_section_header("PREVIEW")
    
    print("┌" + "─" * box_width + "┐")
    for line in lines:
        print(f"│ {line:<{box_width-1}}│")
    print("└" + "─" * box_width + "┘")
    # ไม่ต้องมี print_closer เพราะกรอบปิดตัวเองแล้ว

def print_upload_header():
    print_section_header("UPLOADING")

def print_media_found(count):
    print(f"   ➤ Media Found   : {count} Images")

def print_upload_item(filename, media_id):
    print(f"   ✔ Uploaded      : {filename} [ID: {str(media_id)[:3]}...]")

def print_upload_error(filename, error):
    print(f"   ❌ Error {filename} : {error}")

def print_pose_header():
    # ใช้ Art ของ EXECUTION แทน POSE (เพราะไม่มีรูป POSE)
    print_section_header("POSE") 

def print_post_success(tweet_id):
    print("\n       ✅ [TWEET POSTED SUCCESSFULLY]")
    print(f"   ➤ Tweet ID      : {tweet_id}")

def print_end():
    print_section_header("COMPLETED")
    print("✅ WORKFLOW COMPLETED")
    print("="*50 + "\n")
