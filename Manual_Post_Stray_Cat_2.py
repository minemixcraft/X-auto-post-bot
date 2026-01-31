# Import ข้อมูลตั้งค่า
from bot_config import SHARED_HASHTAGS, GREENHAVEN_DATA
# Import ระบบโพสต์กลาง
from bot_utils import run_manual_workflow

if __name__ == "__main__":
    # สั่งให้ระบบทำงาน โดยส่งชื่อและข้อมูลของ GreenHaven เข้าไป
    run_manual_workflow("Stray Cat 2", STRAY_CAT_DATA, SHARED_HASHTAGS)
