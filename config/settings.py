# Global System and Twitter Config Settings

SYSTEM_CONFIG = {
    "MAX_RUNTIME_MIN": 110,     # เวลาทำงานสูงสุดก่อนตัดจบ
    "TIMEZONE_HOURS": 7,        # UTC Offset (ไทย = +7)
    "DRY_RUN": False,           # True = รันเทสแต่ไม่โพสต์จริง, False = โพสต์จริง
}

UI_CONFIG = {
    "MODULE_NAME": "text",      # สไตล์ UI: "text" (ข้อความสะอาด) หรือ "ascii" (กราฟิก ASCII)
    "PROGRESS_STYLE": "VERTICAL", # สไตล์ Progress Bar: "BLOCK", "SHADE", "RECT", "CIRCLE", "VERTICAL", "SQUARE"
    "SHOW_PREVIEW": False       # แสดงกล่องตัวอย่างทวีตก่อนโพสต์หรือไม่
}

TWITTER_LIMITS = {
    "MAX_CHARS": 280,           # โควตาตัวอักษรสูงสุด
    "URL_WEIGHT": 23,           # ความยาวของลิงก์ (t.co)
    "EMOJI_WEIGHT": 2,          # น้ำหนักของ Emoji/อักษรพิเศษ
    "THAI_WEIGHT": 1            # น้ำหนักอักษรไทย
}

SCHEDULE_CONFIG = {
    "MORNING": {
        "CUTOFF_HOUR": 10,
        "NAME": "Morning Round",
        "TARGET_HOUR": 8,
        "MAX_WAIT_MIN": 45,
        "MSG_INDEX": 0,
        "UPLOAD_IMAGE": True
    },
    "AFTERNOON": {
        "CUTOFF_HOUR": 15,
        "NAME": "Afternoon Round",
        "TARGET_HOUR": 12,
        "MAX_WAIT_MIN": 60,
        "MSG_INDEX": 1,
        "UPLOAD_IMAGE": False
    },
    "EVENING": {
        "NAME": "Evening Round",
        "TARGET_HOUR": 17,
        "MAX_WAIT_MIN": 90,
        "MSG_INDEX": 2,
        "UPLOAD_IMAGE": False
    }
}

SHARED_HASHTAGS = [
    "#ปล่อยกู้", "#เงินกู้นักศึกษา", "#เงินกู้ด่วน", "#กู้เงิน", "#กู้เงินนักศึกษา",
    "#มข", "#มมส", "#มจพ", "#มทส", "#มธร",
    "#ปล่อยกู้รายวัน", "#กู้เงินออนไลน์", "#เงินด่วน", "#เงินกู้รายวัน"
]
