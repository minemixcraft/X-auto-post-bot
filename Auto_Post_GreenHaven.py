# Import ข้อมูลตั้งค่า
from bot_config import SHARED_HASHTAGS, GREENHAVEN_DATA
from bot_utils import run_autopost_workflow, run_x_diagnostics

if __name__ == "__main__":
    print("เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ GreenHaven (Auto Mode)...")
    
    # 1. ดึงที่อยู่รูปภาพแรกจากฐานข้อมูลมาใช้ทดสอบ
    test_image = None
    if "images" in GREENHAVEN_DATA and len(GREENHAVEN_DATA["images"]) > 0:
        test_image = GREENHAVEN_DATA["images"][0]
        
    # 2. รันโหมดวิเคราะห์ (เพื่อเก็บ Log ใน GitHub Actions)
    run_x_diagnostics(test_image_path=test_image)
    
    # =====================================================================
    # 💡 เมื่อซ่อมระบบเสร็จแล้ว ให้สลับ Comment สองบรรทัดล่างนี้เพื่อให้บอททำงานปกติ
    # =====================================================================
    # run_autopost_workflow("GreenHaven", GREENHAVEN_DATA, SHARED_HASHTAGS)
