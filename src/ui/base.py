from config.settings import UI_CONFIG

ACTIVE_STYLE = UI_CONFIG.get("PROGRESS_STYLE", "VERTICAL")

BAR_STYLES = {
    "BLOCK":    {"fill": "█", "empty": "░"},
    "SHADE":    {"fill": "▒", "empty": "░"},
    "RECT":     {"fill": "▰", "empty": "▱"},
    "CIRCLE":   {"fill": "o", "empty": "."},
    "VERTICAL": {"fill": "▮", "empty": "▯"},
    "SQUARE":   {"fill": "■", "empty": "□"},
}

def format_time_str(total_seconds):
    if total_seconds < 0: total_seconds = 0
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"
