import re
from config.settings import TWITTER_LIMITS

def analyze_tweet_weight(text):
    """วิเคราะห์น้ำหนักโดยใช้ค่าจาก TWITTER_LIMITS ใน Config"""
    url_pattern = r'https?://\S+|www\.\S+|lin\.ee/\S+'
    urls = re.findall(url_pattern, text)
    text_without_urls = re.sub(url_pattern, '', text)
    
    LINK_W = TWITTER_LIMITS["URL_WEIGHT"]
    EMOJI_W = TWITTER_LIMITS["EMOJI_WEIGHT"]
    THAI_W = TWITTER_LIMITS["THAI_WEIGHT"]
    
    stats = {
        "link_count": len(urls),
        "link_weight": len(urls) * LINK_W,
        "emoji_count": 0, "emoji_weight": 0,
        "text_count": 0, "text_weight": 0,
        "space_count": 0, "space_weight": 0,
        "total_weight": 0
    }
    
    for char in text_without_urls:
        code = ord(char)
        if char.isspace():
            stats['space_count'] += 1
            stats['space_weight'] += 1
        elif (0x0E00 <= code <= 0x0E7F): # Thai
            stats['text_count'] += 1
            stats['text_weight'] += THAI_W
        elif (code <= 127): # ASCII
            stats['text_count'] += 1
            stats['text_weight'] += 1
        else: # Emoji/Special
            stats['emoji_count'] += 1
            stats['emoji_weight'] += EMOJI_W
            
    stats['total_weight'] = (stats['link_weight'] + stats['emoji_weight'] + 
                             stats['text_weight'] + stats['space_weight'])
    return stats

def calculate_x_char_weight(text):
    return analyze_tweet_weight(text)['total_weight']
