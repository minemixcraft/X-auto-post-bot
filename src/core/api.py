import os
import tweepy

def get_twitter_api():
    keys = [
        os.getenv("CONSUMER_KEY"),
        os.getenv("CONSUMER_SECRET"),
        os.getenv("X_ACCESS_TOKEN"),
        os.getenv("X_ACCESS_TOKEN_SECRET")
    ]
    if not all(keys):
        raise ValueError("Missing API Keys in Environment Variables")
    
    proxy_url = os.getenv("PROXY_URL") or os.getenv("HTTPS_PROXY") or os.getenv("HTTP_PROXY")
    
    if proxy_url:
        client = tweepy.Client(
            consumer_key=keys[0],
            consumer_secret=keys[1],
            access_token=keys[2],
            access_token_secret=keys[3],
            proxies={"http": proxy_url, "https": proxy_url}
        )
        auth = tweepy.OAuth1UserHandler(keys[0], keys[1], keys[2], keys[3])
        api_v1 = tweepy.API(auth, proxy=proxy_url)
    else:
        client = tweepy.Client(
            consumer_key=keys[0],
            consumer_secret=keys[1],
            access_token=keys[2],
            access_token_secret=keys[3]
        )
        auth = tweepy.OAuth1UserHandler(keys[0], keys[1], keys[2], keys[3])
        api_v1 = tweepy.API(auth)
        
    return client, api_v1
