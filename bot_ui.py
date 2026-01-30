# ======================================================
# 🎨 ไฟล์: bot_ui.py
# (เก็บกราฟิก ASCII Art และฟังก์ชันแสดงผลทั้งหมด)
# ======================================================

# 0. ASCII ART ASSETS
ASCII_ART = {
    "HEADER": """
░█▀▀░█▀▄░█▀▀░█▀▀░█▀█░█░█░█▀█░█░█░█▀▀░█▀█
░█░█░█▀▄░█▀▀░█▀▀░█░█░█▀█░█▀█░▀▄▀░█▀▀░█░█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀
    """,
    "SYSTEM_CHECK": """
░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█▄█
░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█
░▀▀▀░░▀░░▀▀▀░░▀░░▀▀▀░▀░▀
     ░█▀▀░█░█░█▀▀░█▀▀░█░█
     ░█░░░█▀█░█▀▀░█░░░█▀▄
     ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀
    """,
    "WAITING": """
░█░█░█▀█░█▀▀░▀█▀░█▀▀░█▀▄
░█▄█░█▀█░█░█░░█░░█▀▀░█░█
░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀░
    """,
    "EXECUTION": """
░█▀▀░█▀▄░█▀▀░█▀▀░█░█░▀█▀░█▀▀░█▀█
░█▀▀░▄▀▀░█▀▀░█░░░█░█░░█░░█░█░█░█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀
    """,
    "PREVIEW": """
░▀█▀░█░█░█▀▀░█▀▀░▀█▀
░░█░░█▄█░█▀▀░█▀▀░░█░
░░▀░░▀░▀░▀▀▀░▀▀▀░░▀░
   ░█▀█░█▀▄░█▀▀░█░█░█▀█░█▀▀░█░█
   ░█▀▀░█▀▄░█▀▀░▀▄▀░█░█░█▀▀░█▄█
   ░▀░░░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀
    """,
    "UPLOADING": """
░█░█░█▀▀░█▀▄░█▀█░█▀█░█▀▄
░█░█░█▀▀░█░█░█░█░█▀█░█░█
░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀░▀▀░
    """,
    "COMPLETED": """
░█▀▀░█▀█░█▄█░█▀▀░█░░░█▀▀░▀█▀░█▀▀░█▀▄
░█░░░█░█░█░█░█▀▀░█░░░█▀▀░░█░░█▀▀░█░█
░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀░
    """
}

# 1. HELPER FUNCTIONS (Formatting)

def format_time_str(total_seconds):
    """แปลงวินาที เป็นข้อความเวลาสวยๆ (ใช้ร่วมกันทั้ง UI และ Logic)"""
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def print_art(key):
    """ปริ้น ASCII Art ตามคีย์ที่ระบุ"""
    if key in ASCII_ART:
        print(ASCII_ART[key].strip())

# 2. DISPLAY FUNCTIONS (การแสดงผล)

def print_header(bot_name):
    print("\n" + "="*50)
    print_art("HEADER")
    print(f"   🤖 BOT: {bot_name.upper()}")
    print("="*50 + "\n")

def print_section(art_key):
    """ปริ้นหัวข้อ Section แบบมี Art"""
    print("\n" + "-"*40)
    print_art(art_key)
    print("-"*40)

def print_info(label, value):
    print(f"   ➤ {label:<15} : {value}")

def print_success(message):
    print(f"   ✅ {message}")

def print_error(message):
    print(f"   ❌ {message}")

def print_preview_box(message):
    lines = message.split('\n')
    width = 50
    
    print_section("PREVIEW")
    print("┌" + "─" * width + "┐")
    for line in lines:
        print(f"│ {line:<{width-2}} │")
    print("└" + "─" * width + "┘")

def print_shades_bar(percent, remaining_seconds, is_finished=False):
    """แสดง Progress Bar แบบ Shades"""
    bar_length = 25
    filled_length = int(bar_length * percent // 100)
    
    if is_finished:
        bar_char = '█'
        status_text = "READY TO START!"
    else:
        bar_char = '▒'
        status_text = "Waiting..."

    bar = bar_char * filled_length + '░' * (bar_length - filled_length)
    time_str = format_time_str(remaining_seconds)
    
    print(f"   {bar} {percent}% | ETA: {time_str} | {status_text}")
