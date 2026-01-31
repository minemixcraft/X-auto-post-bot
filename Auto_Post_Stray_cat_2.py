# Import ข้อมูลตั้งค่า
from bot_config import SHARED_HASHTAGS, STRAY_CAT_DATA
# Import ระบบโพสต์กลาง
from bot_utils import run_autopost_workflow

if __name__ == "__main__":
    # สั่งให้ระบบทำงาน โดยส่งชื่อและข้อมูลของ Stray Cat เข้าไป
    run_autopost_workflow("Stray Cat 2", STRAY_CAT_DATA, SHARED_HASHTAGS)
