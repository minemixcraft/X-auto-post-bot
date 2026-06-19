import os
import random
from src.core.api import get_twitter_api
from src.utils.helpers import get_thai_time

def run_x_diagnostics(test_image_path=None):
    """
    ฟังก์ชันตรวจสอบสถานะ X API แบบครบชุด 
    สามารถใส่ path รูปภาพ เช่น "assets/greenhaven/GH_1.jpg" เพื่อทดสอบอัปโหลดรูปได้
    """
    print("\n" + "="*60)
    print("🛸 X API FULL-SUITE DIAGNOSTIC MODE")
    print("="*60)

    try:
        client, api_v1 = get_twitter_api()

        # --------------------------------------------------
        # [1] ENV VARIABLES CHECK
        # --------------------------------------------------
        print("\n[1] ENV VARIABLES CHECK")
        print(f"   ➤ CONSUMER_KEY         : {'✅ FOUND' if os.getenv('CONSUMER_KEY') else '❌ MISSING'}")
        print(f"   ➤ CONSUMER_SECRET      : {'✅ FOUND' if os.getenv('CONSUMER_SECRET') else '❌ MISSING'}")
        print(f"   ➤ X_ACCESS_TOKEN       : {'✅ FOUND' if os.getenv('X_ACCESS_TOKEN') else '❌ MISSING'}")
        print(f"   ➤ X_ACCESS_TOKEN_SECRET: {'✅ FOUND' if os.getenv('X_ACCESS_TOKEN_SECRET') else '❌ MISSING'}")

        # --------------------------------------------------
        # [2] AUTHENTICATION TEST (OAuth 1.0a)
        # --------------------------------------------------
        print("\n[2] AUTHENTICATION TEST (OAuth 1.0a)")
        try:
            user = api_v1.verify_credentials()
            print("   ✅ verify_credentials() SUCCESS")
            print(f"   ➤ Authenticated User : @{user.screen_name}")
        except Exception as e:
            print("   ❌ verify_credentials() FAILED")
            print(f"   ➤ Type  : {type(e)}")
            print(f"   ➤ Error : {repr(e)}")
            if hasattr(e, "response") and e.response is not None:
                print(f"   ➤ STATUS: {e.response.status_code} | BODY: {e.response.text}")
            return # หยุดการทำงานหาก Auth ไม่ผ่าน

        # --------------------------------------------------
        # [3] API v2 & USER INFO TEST
        # --------------------------------------------------
        print("\n[3] API v2 & USER INFO TEST")
        try:
            me = client.get_me(user_fields=["public_metrics"])
            print("   ✅ get_me() SUCCESS")
            print(f"   ➤ Name/ID : {me.data.name} (@{me.data.username}) [ID: {me.data.id}]")
            print(f"   ➤ Metrics : {me.data.public_metrics}")
        except Exception as e:
            print("   ❌ get_me() FAILED")
            print(f"   ➤ Type  : {type(e)}")
            print(f"   ➤ Error : {repr(e)}")
            if hasattr(e, "response") and e.response is not None:
                print(f"   ➤ STATUS: {e.response.status_code} | BODY: {e.response.text}")

        # --------------------------------------------------
        # [4] RATE LIMIT STATUS CHECK
        # --------------------------------------------------
        print("\n[4] RATE LIMIT STATUS CHECK (API v1.1)")
        try:
            limits = api_v1.rate_limit_status()
            print("   ✅ rate_limit_status() SUCCESS (App is not fully restricted)")
        except Exception as e:
            print("   ❌ rate_limit_status() FAILED")
            print(f"   ➤ Error : {repr(e)}")

        # --------------------------------------------------
        # [5] MEDIA UPLOAD TEST (API v1.1)
        # --------------------------------------------------
        print("\n[5] MEDIA UPLOAD TEST")
        uploaded_media_id = None
        if test_image_path and os.path.exists(test_image_path):
            try:
                media = api_v1.media_upload(test_image_path)
                uploaded_media_id = media.media_id
                print(f"   ✅ media_upload() SUCCESS")
                print(f"   ➤ Media ID : {uploaded_media_id}")
            except Exception as e:
                print("   ❌ media_upload() FAILED")
                print(f"   ➤ Error : {repr(e)}")
        else:
            print(f"   ⚠️ SKIPPED (No valid image path provided: {test_image_path})")

        # --------------------------------------------------
        # [6] POSTING TEST (API v2)
        # --------------------------------------------------
        print("\n[6] POST TEST")
        try:
            test_text = f"Diagnostic Test Post - {random.randint(1000, 9999)}"
            
            if uploaded_media_id:
                response = client.create_tweet(text=test_text, media_ids=[uploaded_media_id])
                print("   ✅ create_tweet() (with Media) SUCCESS")
            else:
                response = client.create_tweet(text=test_text)
                print("   ✅ create_tweet() (Text Only) SUCCESS")
                
            print(f"   ➤ Tweet ID : {response.data['id']}")
            
        except Exception as e:
            print("   ❌ create_tweet() FAILED")
            print(f"   ➤ Type  : {type(e)}")
            print(f"   ➤ Error : {repr(e)}")
            if hasattr(e, "response") and e.response is not None:
                print(f"   ➤ STATUS: {e.response.status_code} | BODY: {e.response.text}")

        # --------------------------------------------------
        # [7] SUMMARY SUMMARY
        # --------------------------------------------------
        print("\n[7] APP STATUS CHECKLIST")
        print("   If you see any ❌ above, verify these in Developer Portal:")
        print("   - [ ] Is the App Suspended? (Check Developer Portal Dashboard)")
        print("   - [ ] Is Billing / Free Tier active? (Check Project settings)")
        print("   - [ ] Is App Permission set to 'Read and Write'?")
        print("   - [ ] Have you Regenerated Tokens AFTER changing permissions?")
        print("="*60 + "\n")

    except Exception as e:
        print("\n❌ CRITICAL ERROR IN DIAGNOSTICS")
        print(type(e))
        print(repr(e))
