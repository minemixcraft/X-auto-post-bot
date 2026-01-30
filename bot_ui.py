# ======================================================
# 🎨 ไฟล์: bot_ui.py (ASCII Art Style)
# (อัปเดตให้โครงสร้างเท่ากับ bot_ui_text.py เป๊ะๆ)
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

# 1. HELPER FUNCTIONS

def format_time_str(total_seconds):
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def print_art(key):
    if key in ASCII_ART:
        print(ASCII_ART[key].strip())

# 2. DISPLAY FUNCTIONS (Standard Interface)

def print_header(bot_name):
    print("\n" + "="*50)
    print_art("HEADER")
    print(f"          {bot_name.upper()}")
    print("="*50 + "\n")

def print_section(key):
    """ปริ้นหัวข้อ Section (รับ key เป็นชื่อ Section)"""
    # Map key ให้ตรงกับ ASCII ART Key
    art_key = key.upper()
    if art_key == "SENDING": art_key = "EXECUTION" # Map คร่าวๆ
    
    print("\n" + "-"*40)
    print_art(art_key)
    print("-"*40)

def print_closer():
    """
    (New) ฟังก์ชันปิด Section 
    - ASCII Art ปกติมีเส้นปิดหัวข้ออยู่แล้ว ฟังก์ชันนี้อาจจะไม่ต้องทำอะไร
    - หรือจะใส่เส้นประบางๆ ก็ได้ เพื่อความเหมือนกัน
    """
    pass # สำหรับ ASCII เราไม่ต้องการเส้นปิดท้ายเพิ่ม เพราะ Art มันใหญ่แล้ว

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

def print_shades_bar(percent, remaining_seconds, is_finished=False, custom_status=None):
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

def print_footer():
    """(New) ฟังก์ชันปิดท้ายงาน"""
    print("\n")
    print_art("COMPLETED")
    print("\n" + "="*50)
