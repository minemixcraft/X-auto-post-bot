# ======================================================
# 🎨 ไฟล์: bot_ui_text.py
# (UI แบบ Custom Box & Double Line Separator)
# ======================================================

def format_time_str(total_seconds):
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

# --- 1. CORE PRINTING FUNCTIONS ---

def print_header(bot_name):
    """แสดง Header ใหญ่ตอนเริ่ม"""
    width = 52
    title = f"🤖 {bot_name.upper()} | SYSTEM V2"
    print("\n" + "╔" + "═"*width + "╗")
    print(f"║ {title:^{width}} ║")
    print("╚" + "═"*width + "╝")

def print_section_header(title):
    """แสดงหัวข้อ พร้อมเส้นคู่ (Double Line) ด้านล่าง"""
    print(f"\n {title}")
    print("=" * 52)

def print_closer():
    """เส้นปิดท้าย Section"""
    print("=" * 52)

# --- 2. SPECIFIC SECTIONS ---

def print_system_check(context_name, target_time, upload_image):
    print_section_header("📌 [SYSTEM CHECK]")
    print(f"   ➤ Context       : {context_name}")
    print(f"   ➤ Target Time   : {target_time}")
    print(f"   ➤ Has Image?    : {'Yes' if upload_image else 'No'}")
    print_closer()

def print_waiting_bar(percent, remaining_seconds, is_finished=False, custom_status=None):
    # (ใช้ Logic เดิม แต่ปรับให้เข้ากับ Theme ใหม่ถ้าจำเป็น)
    # ตรงนี้ใช้โค้ดเดิมได้ แต่ขอตัดมาเฉพาะส่วนแสดงผล
    bar_length = 25
    filled_length = int(bar_length * percent // 100)
    
    if is_finished:
        status_text = custom_status if custom_status else "Target Reached!"
        print(f"   ✅ {status_text}")
    else:
        bar_char = '▒'
        status_text = custom_status if custom_status else "Waiting..."
        time_str = format_time_str(remaining_seconds)
        if percent == 0: print(f"   {status_text}")
        
        bar = bar_char * filled_length + '░' * (bar_length - filled_length)
        print(f"   {bar} {percent}% | ETA: {time_str} | {status_text}")

def print_preview_box(message):
    """
    สร้างกรอบล้อมข้อความ แบบยืดหดตามความยาวข้อความจริง
    """
    lines = message.split('\n')
    
    # คำนวณความกว้างที่ต้องใช้ (หาบรรทัดที่ยาวที่สุด)
    # เพิ่ม Padding ซ้ายขวาข้างละ 2 ตัวอักษร
    max_len = 0
    for line in lines:
        # (หมายเหตุ: ภาษาไทยอาจมีความกว้างไม่เท่า len จริง แต่ใช้ len คร่าวๆ ได้)
        if len(line) > max_len:
            max_len = len(line)
            
    box_width = max_len + 4 # เผื่อขอบ
    
    print_section_header("🗟 [TWEET PREVIEW]")
    print("┌" + "─" * box_width + "┐")
    for line in lines:
        # จัดข้อความชิดซ้าย
        print(f"│ {line:<{box_width-1}}") 
    print("└" + "─" * box_width + "┘")
    # (Preview ไม่ต้องมีเส้นปิดล่าง ตามตัวอย่างที่ส่งมา)

def print_upload_header():
    print_section_header(" [UPLOADING]")

def print_upload_item(filename, media_id):
    print(f"   ✔ Uploaded      : {filename} [ID: {str(media_id)[:3]}...]")

def print_media_found(count):
    print(f"   ➤ Media Found   : {count} Images")

def print_upload_error(filename, error):
    print(f"   ❌ Error {filename} : {error}")

def print_pose_header():
    print_section_header(" [POSE]")

def print_post_success(tweet_id):
    print("\n       ✅ [TWEET POSTED SUCCESSFULLY]")
    print(f"   ➤ Tweet ID      : {tweet_id}")

def print_end():
    print_section_header(" [END]")

# --- Helpers for Logic ---
def print_info(label, value):
    print(f"   ➤ {label:<13} : {value}")
