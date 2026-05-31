# Import ข้อมูลตั้งค่า
from bot_config import SHARED_HASHTAGS, STRAY_CAT_DATA
from bot_utils import run_manual_workflow, run_x_diagnostics

if __name__ == "__main__":
    print("เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ Stray Cat 2...")
    
    # 1. ดึงที่อยู่รูปภาพแรกจากฐานข้อมูลมาใช้ทดสอบ
    test_image = None
    if "images" in STRAY_CAT_DATA and len(STRAY_CAT_DATA["images"]) > 0:
        test_image = STRAY_CAT_DATA["images"][0]
        
    # 2. รันโหมดวิเคราะห์ (ทดสอบดึงข้อมูลและอัปโหลดรูปภาพ)
    run_x_diagnostics(test_image_path=test_image)
    
    # =====================================================================
    # 💡 หากตรวจสอบผ่านหมด (ขึ้น ✅) ให้สลับ Comment สองบรรทัดด้านล่างนี้
    # =====================================================================
    # run_manual_workflow("Stray Cat 2", STRAY_CAT_DATA, SHARED_HASHTAGS)
