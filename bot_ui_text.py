# ======================================================
# 🎨 ไฟล์: bot_ui_text.py
# (Custom UI: d[o_0]b Style)
# ======================================================

# 1. HELPER: MAPPING หัวข้อ (ใส่ Emoji/Space ตามที่คุณต้องการ)
SECTION_TITLES = {
    "SYSTEM_CHECK": "⚙️ [SYSTEM CHECK]",
    "WAITING":      "⏱︎ [WAITING PROCESS]",
    "EXECUTION":    "   [EXECUTION START]",
    "PREVIEW":      " 🗟 [TWEET PREVIEW]",
    "UPLOADING":    "   [UPLOADING]",
    "SUCCESS":      "    [TWEET POSTED SUCCESSFULLY]",
    "END":          "   [END]"
}

# เส้นคั่นยาวๆ แบบ =
SEPARATOR = "=" * 52

# 2. HELPER FUNCTIONS

def format_time_str(total_seconds):
    """แปลงวินาที เป็นข้อความเวลา 00:00:00"""
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

# 3. DISPLAY FUNCTIONS (การแสดงผล)

def print_header(bot_name):
    """แสดง Header แบบ d[o_0]b"""
    width = 50
    # จัดข้อความ d[o_0]b ให้กึ่งกลาง
    title = f"d[o_0]b {bot_name.upper()}"
    
    print("\n" + "╔" + "═"*width + "╗")
    print(f"║ {title:^{width}} ║") 
    print("╚" + "═"*width + "╝")

def print_section(key):
    """แสดงหัวข้อ พร้อมเส้น ==== ด้านล่าง"""
    title = SECTION_TITLES.get(key, key)
    print(f"\n{title}")
    print(SEPARATOR)

def print_closer():
    """แสดงเส้น ==== ปิดท้าย Section"""
    print(SEPARATOR)

def print_info(label, value):
    """แสดงข้อมูลแบบ ➤"""
    print(f"   ➤ {label:<13} : {value}")

def print_success(message):
    print(f"   ✔ {message}")

def print_error(message):
    print(f"   ❌ {message}")

def print_preview_box(message):
    """สร้างกรอบ Preview"""
    lines = message.split('\n')
    width = 50
    
    print_section("PREVIEW")
    print("┌" + "─" * width + "┐")
    for line in lines:
        print(f"│ {line:<{width-2}} │")
    print("└" + "─" * width + "┘")

def print_shades_bar(percent, remaining_seconds, is_finished=False, custom_status=None):
    """แสดง Progress Bar"""
    bar_length = 25
    filled_length = int(bar_length * percent // 100)
    
    bar_char = '▒'
    bar = bar_char * filled_length + '░' * (bar_length - filled_length)
    
    if is_finished:
        # ถ้าเสร็จแล้ว ไม่ต้องแสดง Bar บรรทัดใหม่ (ตามดีไซน์คุณคือจบ Section เลย)
        pass 
    else:
        status_text = custom_status if custom_status else "Waiting..."
        time_str = format_time_str(remaining_seconds)
        
        # แสดง Bar แบบที่คุณต้องการ
        print(f"   {bar} {percent}% | ETA: {time_str} | {status_text}")

def print_footer():
    """แสดงส่วนจบการทำงาน"""
    print_section("END")
    print(SEPARATOR + "\n")
