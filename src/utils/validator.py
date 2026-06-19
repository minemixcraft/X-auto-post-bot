import os
import random
from config.settings import TWITTER_LIMITS
from src.utils.tweet_analyzer import calculate_x_char_weight

def prepare_tweet_content(msg_index, messages_list, hashtag_pool):
    if not messages_list: return ""
    if msg_index >= len(messages_list): msg_index = 0
    
    base_msg = messages_list[msg_index].strip() + "\n\n"
    tags = list(set(hashtag_pool))
    random.shuffle(tags)
    
    final_msg = base_msg
    MAX_CHARS = TWITTER_LIMITS["MAX_CHARS"]
    
    for t in tags:
        test_msg = final_msg + t + " "
        if calculate_x_char_weight(test_msg) <= MAX_CHARS:
            final_msg = test_msg
        else:
            break
    return final_msg.strip()

def filter_existing_images(image_paths):
    if not image_paths: return []
    return [img for img in image_paths if os.path.exists(img)]
