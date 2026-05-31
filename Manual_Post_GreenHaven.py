# # Import ข้อมูลตั้งค่า
# from bot_config import SHARED_HASHTAGS, GREENHAVEN_DATA
# # Import ระบบโพสต์กลาง
# from bot_utils import run_manual_workflow

# if __name__ == "__main__":
#     # สั่งให้ระบบทำงาน โดยส่งชื่อและข้อมูลของ GreenHaven เข้าไป
#     run_manual_workflow("GreenHaven", GREENHAVEN_DATA, SHARED_HASHTAGS)


# Import ข้อมูลตั้งค่า
from bot_config import SHARED_HASHTAGS, GREENHAVEN_DATA
# Import ระบบ Diagnostic 
from bot_utils import run_x_diagnostics

if __name__ == "__main__":
    print("เริ่มรันโหมดตรวจสอบระบบ GreenHaven...")
    run_x_diagnostics()
