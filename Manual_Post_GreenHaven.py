# Import ข้อมูลตั้งค่า
from bot_config import SHARED_HASHTAGS, GREENHAVEN_DATA
from bot_utils import run_manual_workflow, run_x_diagnostics

if __name__ == "__main__":
    print("เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ GreenHaven...")
    
    # 1. ดึงที่อยู่รูปภาพแรกจากฐานข้อมูลของ GreenHaven มาใช้ทดสอบ
    test_image = None
    if "images" in GREENHAVEN_DATA and len(GREENHAVEN_DATA["images"]) > 0:
        test_image = GREENHAVEN_DATA["images"][0]
        
    # 2. รันโหมดวิเคราะห์ (จะมีการทดสอบดึงข้อมูลและอัปโหลดรูปภาพด้วย)
    run_x_diagnostics(test_image_path=test_image)
    
    # =====================================================================
    # 💡 หมายเหตุเมื่อซ่อมระบบเสร็จแล้ว:
    # หากตรวจสอบจนผ่านหมด (ขึ้น ✅ ทุกข้อ) และต้องการให้ระบบกลับมาโพสต์ตามปกติ
    # ให้ใส่เครื่องหมาย # หน้าคำสั่ง run_x_diagnostics(...) ด้านบน
    # แล้วเอาเครื่องหมาย # หน้าคำสั่ง run_manual_workflow(...) ด้านล่างนี้ออกครับ
    # =====================================================================
    
    # run_manual_workflow("GreenHaven", GREENHAVEN_DATA, SHARED_HASHTAGS)
