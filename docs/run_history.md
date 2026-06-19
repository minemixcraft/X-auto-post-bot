Run python Auto_Post_Stray_cat_2.py

python Auto_Post_Stray_cat_2.py

shell: /usr/bin/bash -e {0}

env:

pythonLocation: /opt/hostedtoolcache/Python/3.9.25/x64

PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib/pkgconfig

Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib

PYTHONUNBUFFERED: 1

CONSUMER_KEY: ***

CONSUMER_SECRET: ***

X_ACCESS_TOKEN: ***

X_ACCESS_TOKEN_SECRET: ***

เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ Stray Cat 2 (Auto Mode)...

============================================================

🛸 X API FULL-SUITE DIAGNOSTIC MODE

============================================================

[1] ENV VARIABLES CHECK

➤ CONSUMER_KEY : ✅ FOUND

➤ CONSUMER_SECRET : ✅ FOUND

➤ X_ACCESS_TOKEN : ✅ FOUND

➤ X_ACCESS_TOKEN_SECRET: ✅ FOUND

[2] AUTHENTICATION TEST (OAuth 1.0a)

❌ verify_credentials() FAILED

➤ Type : <class 'tweepy.errors.Unauthorized'>

➤ Error : Unauthorized('401 Unauthorized\n32 - Could not authenticate you.')

➤ STATUS: 401 | BODY: {"errors":[{"code":32,"message":"Could not authenticate you."}]}

╔════════════════════════════════════════════════════╗

║ d[o_0]b STRAY CAT 2 X-BOT ║

╚════════════════════════════════════════════════════╝

⚙️ [SYSTEM CHECK]

====================================================

➤ Time Zone : Asia/Bangkok (UTC+7)

➤ Current Date : 2026-06-18

➤ Current Time : 17:34:19

➤ Context : Evening Round

➤ Target Time : 17:00

➤ Image : No

➤ Msg Loaded : 3 items

➤ Tag Pool : 14 tags

➤ Max Delay : 90 mins

====================================================

⏱︎ [WAITING PROCESS] [1/4]

====================================================

====================================================

[EXECUTION START] [2/4]

====================================================

📊 [TIME BUDGET ANALYSIS]

➤ Total Runtime : 110 mins

➤ Time Elapsed : 0.0 mins

➤ Remaining : 110.0 mins

➤ Config: 90m -> Safe: 90m (OK)

--------------------------------------------------

➤ Strategy : Random Delay (84m 45s)

... (Sleeping) ...

▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 10% | ETA: 01:15:22 | Sleeping...

▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 20% | ETA: 01:07:00 | Sleeping...

▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 30% | ETA: 00:58:37 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 40% | ETA: 00:50:15 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯ 50% | ETA: 00:41:52 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯ 60% | ETA: 00:33:30 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯ 70% | ETA: 00:25:07 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯ 80% | ETA: 00:16:45 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯ 90% | ETA: 00:08:22 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ 100% | ETA: 00:00:00 | Waking Up!

====================================================

[UPLOADING] [3/4]

====================================================

====================================================

[POSE] [4/4]

====================================================

❌ [TWITTER API ERROR]

➤ Type : <class 'tweepy.errors.Unauthorized'>

➤ Error : Unauthorized('401 Unauthorized\nUnauthorized')

➤ STATUS: 401

➤ BODY : {

"title": "Unauthorized",

"type": "about:blank",

"status": 401,

"detail": "Unauthorized"

}

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

❌ CRITICAL SYSTEM ERROR: 401 Unauthorized

Unauthorized

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[END]

====================================================

✅ WORKFLOW COMPLETED

====================================================,Run python Auto_Post_Stray_cat_1.py

เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ Stray Cat 1 (Auto Mode)...

============================================================

🛸 X API FULL-SUITE DIAGNOSTIC MODE

============================================================

[1] ENV VARIABLES CHECK

➤ CONSUMER_KEY : ✅ FOUND

➤ CONSUMER_SECRET : ✅ FOUND

➤ X_ACCESS_TOKEN : ✅ FOUND

➤ X_ACCESS_TOKEN_SECRET: ✅ FOUND

[2] AUTHENTICATION TEST (OAuth 1.0a)

✅ verify_credentials() SUCCESS

➤ Authenticated User : @babeyi0i

[3] API v2 & USER INFO TEST

✅ get_me() SUCCESS

➤ Name/ID : Stray cat (@babeyi0i) [ID: 1878820313158557696]

➤ Metrics : {'followers_count': 4177, 'following_count': 20, 'tweet_count': 1111, 'listed_count': 1, 'like_count': 78, 'media_count': 254}

[4] RATE LIMIT STATUS CHECK (API v1.1)

✅ rate_limit_status() SUCCESS (App is not fully restricted)

[5] MEDIA UPLOAD TEST

✅ media_upload() SUCCESS

➤ Media ID : 2067556162728583168

[6] POST TEST

❌ create_tweet() FAILED

➤ Type : <class 'tweepy.errors.HTTPException'>

➤ Error : HTTPException('402 Payment Required\nYour enrolled account [2016521302417547264] does not have any credits to fulfill this request.')

➤ STATUS: 402 | BODY: {"account_id":2016521302417547264,"title":"CreditsDepleted","detail":"Your enrolled account [2016521302417547264] does not have any credits to fulfill this request.","type":"[https://api.twitter.com/2/problems/credits](https://api.twitter.com/2/problems/credits)"}

[7] APP STATUS CHECKLIST

If you see any ❌ above, verify these in Developer Portal:

- [ ] Is the App Suspended? (Check Developer Portal Dashboard)

- [ ] Is Billing / Free Tier active? (Check Project settings)

- [ ] Is App Permission set to 'Read and Write'?

- [ ] Have you Regenerated Tokens AFTER changing permissions?

============================================================

╔════════════════════════════════════════════════════╗

║ d[o_0]b STRAY CAT 1 X-BOT ║

╚════════════════════════════════════════════════════╝

⚙️ [SYSTEM CHECK]

====================================================

➤ Time Zone : Asia/Bangkok (UTC+7)

➤ Current Date : 2026-06-18

➤ Current Time : 17:32:57

➤ Context : Evening Round

➤ Target Time : 17:00

➤ Image : No

➤ Msg Loaded : 3 items

➤ Tag Pool : 14 tags

➤ Max Delay : 90 mins

====================================================

⏱︎ [WAITING PROCESS] [1/4]

====================================================

====================================================

[EXECUTION START] [2/4]

====================================================

📊 [TIME BUDGET ANALYSIS]

➤ Total Runtime : 110 mins

➤ Time Elapsed : 0.0 mins

➤ Remaining : 110.0 mins

➤ Config: 90m -> Safe: 90m (OK)

--------------------------------------------------

➤ Strategy : Random Delay (26m 4s)

... (Sleeping) ...

▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 10% | ETA: 00:22:33 | Sleeping...

▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 20% | ETA: 00:20:03 | Sleeping...

▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 30% | ETA: 00:17:32 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 40% | ETA: 00:15:02 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯ 50% | ETA: 00:12:32 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯ 60% | ETA: 00:10:01 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯ 70% | ETA: 00:07:31 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯ 80% | ETA: 00:05:00 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯ 90% | ETA: 00:02:30 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ 100% | ETA: 00:00:00 | Waking Up!

====================================================

[UPLOADING] [3/4]

====================================================

====================================================

[POSE] [4/4]

====================================================

❌ [TWITTER API ERROR]

➤ Type : <class 'tweepy.errors.HTTPException'>

➤ Error : HTTPException('402 Payment Required\nYour enrolled account [2016521302417547264] does not have any credits to fulfill this request.')

➤ STATUS: 402

➤ BODY : {"account_id":2016521302417547264,"title":"CreditsDepleted","detail":"Your enrolled account [2016521302417547264] does not have any credits to fulfill this request.","type":"[https://api.twitter.com/2/problems/credits](https://api.twitter.com/2/problems/credits)"}

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

❌ CRITICAL SYSTEM ERROR: 402 Payment Required

Your enrolled account [2016521302417547264] does not have any credits to fulfill this request.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[END]

====================================================

✅ WORKFLOW COMPLETED

====================================================,Run python Auto_Post_Moonchill.py

python Auto_Post_Moonchill.py

shell: /usr/bin/bash -e {0}

env:

pythonLocation: /opt/hostedtoolcache/Python/3.9.25/x64

PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib/pkgconfig

Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib

PYTHONUNBUFFERED: 1

CONSUMER_KEY: ***

CONSUMER_SECRET: ***

X_ACCESS_TOKEN: ***

X_ACCESS_TOKEN_SECRET: ***

เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ MoonChill (Auto Mode)...

============================================================

🛸 X API FULL-SUITE DIAGNOSTIC MODE

============================================================

[1] ENV VARIABLES CHECK

➤ CONSUMER_KEY : ✅ FOUND

➤ CONSUMER_SECRET : ✅ FOUND

➤ X_ACCESS_TOKEN : ✅ FOUND

➤ X_ACCESS_TOKEN_SECRET: ✅ FOUND

[2] AUTHENTICATION TEST (OAuth 1.0a)

❌ verify_credentials() FAILED

➤ Type : <class 'tweepy.errors.Forbidden'>

➤ Error : Forbidden('403 Forbidden')

➤ STATUS: 403 | BODY: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-1pwIhbiKKWngW3ym8RGxiR&#39; &#39;unsafe-eval&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) connect-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) frame-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; child-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+");background-repeat:no-repeat;background-size:contain;padding-left:34px}</style><meta http-equiv="refresh" content="360"></head><body><div class="main-wrapper" role="main"><div class="main-content"><noscript><div class="h2"><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script nonce="1pwIhbiKKWngW3ym8RGxiR">(function(){window._cf_chl_opt = {cFPWv: 'b',cH: '61wWMVaNTB6NnwZiGVn_MV9V_c_7dqWlBPg7MV.Ef2g-1781778976-1.2.1.1-xmtMIh5eDJd4MWoDED9W2wJ1jXdXucV4KeIqbEHZvN9uq013MJ3SiYHiAIuYXFss',cITimeS: '1781778976',cN: '1pwIhbiKKWngW3ym8RGxiR',cRay: 'a0d9a6ec3dbef084',cTplB: '0',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/1.1/account/verify_credentials.json?__cf_chl_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU",cvId: '3',cZone: 'api.twitter.com',fa:"/1.1/account/verify_credentials.json?__cf_chl_f_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU",md: '4An5Ylyuva9m5J5H_Cs1N8yZnctTdQ71g5353UHfDew-1781778976-1.2.1.1-2nmBs1RXWz8pcX.BB8XBxRXwDbjv1Pr8yQrprgoCZJBy__hT.sIaLusjRLqwbzNwde6sy8k9GD3gzAutPTAJ_SpVhh4sP.twfZNbH9qaeM.0VWmumvPEeeS1harQqTKINXsJrlGxyV47fLoZD7QDKKF.QtybcrKWCASGTglpcbf2xulf4o_0YXOpq0mKe2phXRBlEKZKNV4OnBkBLwhHBm23XVITf37fSU8LQL_E3UPduajFPjjdnV0q1YbKNnxMss7s2v7oo3ozEOx7nqQ2aULa3HtDdoaBmWLD1vEq6p._6FvCr1xWKGFXvPkZ9kMKvpIbK9Ir.e6duJDQBNhBB6eEb6IkkX9122UcUqbXNBueVLshE3eRXwNbZicgdbuL2X.RCQLfzTk5_jc7uFKb3XpLATBQnDrZsWIfPXtGnStxeAQ.ETk9XAXOzkrlLywTTa_cWNvXdhcIUxKKNfSPvg0vwHuc_JhxmLXxJVRfuXSfECwFA2uiBiqiCPwVWyfV9QDueK86MGDn6p2O2dbt0wdcYUB9UsOKJIH_bQSSla68N62Pc7fDPLGj0_bWLAQXfO0b0e2GLd3.c6Cll9Ga6nKClDjEGUjpnNoW1H_tsQDshqi4_RAJ6LOqj1BxFJJZWHQFw7YDgVIX1RtX_dHGA3UdhUcxh0pbPn9LR3PiOokV3alAy1nDxmLNXaOu34V4zmyYbbIY0hwOKRjdIQyBRIteg5iRJiIyd.LpCqHXt.B2MIN.l.oH4o5K50z6smIY4pQbwfdtSiS0Y7py3E06uVQSYqustxbf9XirrowtYuBXX5PqjGk3MCg7cJiD2.uSByIyPQoMo5mln5UvbttNJJI7LgbpC9ZNBcIDBQ8YS.qqBs2lpC0JaLyj5U9Edu7dLmqo8G6oX12nXM6k2_edA2cRwYHn0jMx_yr3S3liGnPh_d5pisWdnPhKOg6XU0TET1JKZSCkL8JrcjNf3eQaPbj4WlwzPctJK5bjBWYiwlFXiq6.7C5qthHubboz8b_N',mdrd: '',};var a = document.createElement('script');a.nonce = '1pwIhbiKKWngW3ym8RGxiR';a.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=a0d9a6ec3dbef084';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/1.1/account/verify_credentials.json?__cf_chl_rt_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());</script></body></html>

╔════════════════════════════════════════════════════╗

║ d[o_0]b MOONCHILL X-BOT ║

╚════════════════════════════════════════════════════╝

⚙️ [SYSTEM CHECK]

====================================================

➤ Time Zone : Asia/Bangkok (UTC+7)

➤ Current Date : 2026-06-18

➤ Current Time : 17:36:16

➤ Context : Evening Round

➤ Target Time : 17:00

➤ Image : No

➤ Msg Loaded : 3 items

➤ Tag Pool : 14 tags

➤ Max Delay : 90 mins

====================================================

⏱︎ [WAITING PROCESS] [1/4]

====================================================

====================================================

[EXECUTION START] [2/4]

====================================================

📊 [TIME BUDGET ANALYSIS]

➤ Total Runtime : 110 mins

➤ Time Elapsed : 0.0 mins

➤ Remaining : 110.0 mins

➤ Config: 90m -> Safe: 90m (OK)

--------------------------------------------------

➤ Strategy : Random Delay (1m 20s)

... (Sleeping) ...

▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 10% | ETA: 00:00:18 | Sleeping...

▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 20% | ETA: 00:00:16 | Sleeping...

▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 30% | ETA: 00:00:14 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 40% | ETA: 00:00:12 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯ 50% | ETA: 00:00:10 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯ 60% | ETA: 00:00:08 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯ 70% | ETA: 00:00:06 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯ 80% | ETA: 00:00:04 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯ 90% | ETA: 00:00:02 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ 100% | ETA: 00:00:00 | Waking Up!

====================================================

[UPLOADING] [3/4]

====================================================

====================================================

[POSE] [4/4]

====================================================

❌ [TWITTER API ERROR]

➤ Type : <class 'tweepy.errors.Forbidden'>

➤ Error : Forbidden('403 Forbidden')

➤ STATUS: 403

➤ BODY : <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-qtWhzRLUVA8OKImNpZbJOm&#39; &#39;unsafe-eval&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) connect-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) frame-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; child-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+");background-repeat:no-repeat;background-size:contain;padding-left:34px}</style><meta http-equiv="refresh" content="360"></head><body><div class="main-wrapper" role="main"><div class="main-content"><noscript><div class="h2"><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script nonce="qtWhzRLUVA8OKImNpZbJOm">(function(){window._cf_chl_opt = {cFPWv: 'b',cH: 'o73X9zLPuiptmMu2AdOs8vknckZUDw4JfKHxc_..gpk-1781778996-1.2.1.1-EwQWGis8lmvzLdGgaFiBL65sZ0LlLOpF1.WdSrsQXHiVk8jO9MfNXogZ816rby2h',cITimeS: '1781778996',cN: 'qtWhzRLUVA8OKImNpZbJOm',cRay: 'a0d9a76a0a6446cc',cTplB: '0',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/2/tweets?__cf_chl_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA",cvId: '3',cZone: 'api.twitter.com',fa:"/2/tweets?__cf_chl_f_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA",md: 'xOZaFMM3FmH.UnwlAn2hQ10xhwN6hMZab3w8SuYLTYE-1781778996-1.2.1.1-GoidsXkPU8dbLazlrhl.CZnZwDnvUCySgAJoAiKxsN6Z5Mg5q0AkuwkMJz.PaHd2CYMjNuy1K8I_LVp9FuzEX9cE2fXY7Xr8qGBQAKiG_O83cR8kJQU5JHq6wA556zhclZIOIVU_6M0LT_mTu1Xdhmhs3LDkm4GeNXgG.CguF0qv6t.RuO8N2k9IPeBjMKj4wYoDhRJHiBaJz8pwkyKw.pvlxsO4eSZmwWPvQt3C92w2DzpjyefbYiGZU0FseXIXxuevXYUks6i4KL2HSSIoXhKQwVxftQegHMsXj6QkJ3cPILTRxsyPu8GELjxJtTRQz9J_JHStBqnvmBNA0Eg62blK0dGlSkvYWIsksElv49z14o_CjVfCqf0mj..DfrExC.wmRFsBNvgW3NWKcmf_osow0ViOU2W4zEO9BWmtiSDTAkElrv7qq9qmjFEi5Y1xKP3xtjKa52C.5z1WxChUG1T_1sJhwuuiE6B5f.m1vr3yU0M8gwkbor8L9KgBfMPybI5asfjylQrXAHyGe8kbOo4YtRlHM5XU4xgK3wKpzEbBN09jrYoOT0QCIVLzWjFOzOYKubmA3CwGUvoATGNx7tEF9cn_FNSmgNC01tCcue1Hz4LTgWk49XIE4_BhSB40fipNG1GxF8VIvJO3o.C86RLOJOMPsOcx.zVocLObZJXN.l.zdvyqAfvaLmVvd3165insTF_48FUkfudVid_AibeDix1XpDOIALNY7oQWDh5SXsd.s4CXisi0RpdpC3XQohjvP1EMNTrR3KslPzT5j9cMqxxxVplqXZH8qmy7TebVJGSvKsT2lmjadQJ2FNFLHxuN7giATE04rBoFs0NqVpZTjGK.2jIybfStptBf5uWFh1wzE6UdKV5CIvDPGC.9XhJGVeurqrEXVsc2b4eTEfzKrjbqNxTIW7qBNpHKuNv2ykx329IgN5VLjSeahtEgkyGIy5.RptcHkYSrM9f.wg',mdrd: '',};var a = document.createElement('script');a.nonce = 'qtWhzRLUVA8OKImNpZbJOm';a.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=a0d9a76a0a6446cc';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/2/tweets?__cf_chl_rt_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());</script></body></html>

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

❌ CRITICAL SYSTEM ERROR: 403 Forbidden

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[END]

====================================================

✅ WORKFLOW COMPLETED

====================================================,
[Run python Auto_Post_Moonchill.py

python Auto_Post_Moonchill.py

shell: /usr/bin/bash -e {0}

env:

pythonLocation: /opt/hostedtoolcache/Python/3.9.25/x64

PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib/pkgconfig

Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib

PYTHONUNBUFFERED: 1

CONSUMER_KEY: ***

CONSUMER_SECRET: ***

X_ACCESS_TOKEN: ***

X_ACCESS_TOKEN_SECRET: ***

เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ MoonChill (Auto Mode)...

============================================================

🛸 X API FULL-SUITE DIAGNOSTIC MODE

============================================================

[1] ENV VARIABLES CHECK

➤ CONSUMER_KEY : ✅ FOUND

➤ CONSUMER_SECRET : ✅ FOUND

➤ X_ACCESS_TOKEN : ✅ FOUND

➤ X_ACCESS_TOKEN_SECRET: ✅ FOUND

[2] AUTHENTICATION TEST (OAuth 1.0a)

❌ verify_credentials() FAILED

➤ Type : <class 'tweepy.errors.Forbidden'>

➤ Error : Forbidden('403 Forbidden')

➤ STATUS: 403 | BODY: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-1pwIhbiKKWngW3ym8RGxiR&#39; &#39;unsafe-eval&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) connect-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) frame-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; child-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+");background-repeat:no-repeat;background-size:contain;padding-left:34px}</style><meta http-equiv="refresh" content="360"></head><body><div class="main-wrapper" role="main"><div class="main-content"><noscript><div class="h2"><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script nonce="1pwIhbiKKWngW3ym8RGxiR">(function(){window._cf_chl_opt = {cFPWv: 'b',cH: '61wWMVaNTB6NnwZiGVn_MV9V_c_7dqWlBPg7MV.Ef2g-1781778976-1.2.1.1-xmtMIh5eDJd4MWoDED9W2wJ1jXdXucV4KeIqbEHZvN9uq013MJ3SiYHiAIuYXFss',cITimeS: '1781778976',cN: '1pwIhbiKKWngW3ym8RGxiR',cRay: 'a0d9a6ec3dbef084',cTplB: '0',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/1.1/account/verify_credentials.json?__cf_chl_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU",cvId: '3',cZone: 'api.twitter.com',fa:"/1.1/account/verify_credentials.json?__cf_chl_f_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU",md: '4An5Ylyuva9m5J5H_Cs1N8yZnctTdQ71g5353UHfDew-1781778976-1.2.1.1-2nmBs1RXWz8pcX.BB8XBxRXwDbjv1Pr8yQrprgoCZJBy__hT.sIaLusjRLqwbzNwde6sy8k9GD3gzAutPTAJ_SpVhh4sP.twfZNbH9qaeM.0VWmumvPEeeS1harQqTKINXsJrlGxyV47fLoZD7QDKKF.QtybcrKWCASGTglpcbf2xulf4o_0YXOpq0mKe2phXRBlEKZKNV4OnBkBLwhHBm23XVITf37fSU8LQL_E3UPduajFPjjdnV0q1YbKNnxMss7s2v7oo3ozEOx7nqQ2aULa3HtDdoaBmWLD1vEq6p._6FvCr1xWKGFXvPkZ9kMKvpIbK9Ir.e6duJDQBNhBB6eEb6IkkX9122UcUqbXNBueVLshE3eRXwNbZicgdbuL2X.RCQLfzTk5_jc7uFKb3XpLATBQnDrZsWIfPXtGnStxeAQ.ETk9XAXOzkrlLywTTa_cWNvXdhcIUxKKNfSPvg0vwHuc_JhxmLXxJVRfuXSfECwFA2uiBiqiCPwVWyfV9QDueK86MGDn6p2O2dbt0wdcYUB9UsOKJIH_bQSSla68N62Pc7fDPLGj0_bWLAQXfO0b0e2GLd3.c6Cll9Ga6nKClDjEGUjpnNoW1H_tsQDshqi4_RAJ6LOqj1BxFJJZWHQFw7YDgVIX1RtX_dHGA3UdhUcxh0pbPn9LR3PiOokV3alAy1nDxmLNXaOu34V4zmyYbbIY0hwOKRjdIQyBRIteg5iRJiIyd.LpCqHXt.B2MIN.l.oH4o5K50z6smIY4pQbwfdtSiS0Y7py3E06uVQSYqustxbf9XirrowtYuBXX5PqjGk3MCg7cJiD2.uSByIyPQoMo5mln5UvbttNJJI7LgbpC9ZNBcIDBQ8YS.qqBs2lpC0JaLyj5U9Edu7dLmqo8G6oX12nXM6k2_edA2cRwYHn0jMx_yr3S3liGnPh_d5pisWdnPhKOg6XU0TET1JKZSCkL8JrcjNf3eQaPbj4WlwzPctJK5bjBWYiwlFXiq6.7C5qthHubboz8b_N',mdrd: '',};var a = document.createElement('script');a.nonce = '1pwIhbiKKWngW3ym8RGxiR';a.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=a0d9a6ec3dbef084';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/1.1/account/verify_credentials.json?__cf_chl_rt_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());</script></body></html>

╔════════════════════════════════════════════════════╗

║ d[o_0]b MOONCHILL X-BOT ║

╚════════════════════════════════════════════════════╝

⚙️ [SYSTEM CHECK]

====================================================

➤ Time Zone : Asia/Bangkok (UTC+7)

➤ Current Date : 2026-06-18

➤ Current Time : 17:36:16

➤ Context : Evening Round

➤ Target Time : 17:00

➤ Image : No

➤ Msg Loaded : 3 items

➤ Tag Pool : 14 tags

➤ Max Delay : 90 mins

====================================================

⏱︎ [WAITING PROCESS] [1/4]

====================================================

====================================================

[EXECUTION START] [2/4]

====================================================

📊 [TIME BUDGET ANALYSIS]

➤ Total Runtime : 110 mins

➤ Time Elapsed : 0.0 mins

➤ Remaining : 110.0 mins

➤ Config: 90m -> Safe: 90m (OK)

--------------------------------------------------

➤ Strategy : Random Delay (1m 20s)

... (Sleeping) ...

▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 10% | ETA: 00:00:18 | Sleeping...

▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 20% | ETA: 00:00:16 | Sleeping...

▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 30% | ETA: 00:00:14 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 40% | ETA: 00:00:12 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯ 50% | ETA: 00:00:10 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯ 60% | ETA: 00:00:08 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯ 70% | ETA: 00:00:06 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯ 80% | ETA: 00:00:04 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯ 90% | ETA: 00:00:02 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ 100% | ETA: 00:00:00 | Waking Up!

====================================================

[UPLOADING] [3/4]

====================================================

====================================================

[POSE] [4/4]

====================================================

❌ [TWITTER API ERROR]

➤ Type : <class 'tweepy.errors.Forbidden'>

➤ Error : Forbidden('403 Forbidden')

➤ STATUS: 403

➤ BODY : <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-qtWhzRLUVA8OKImNpZbJOm&#39; &#39;unsafe-eval&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) connect-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) frame-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; child-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+");background-repeat:no-repeat;background-size:contain;padding-left:34px}</style><meta http-equiv="refresh" content="360"></head><body><div class="main-wrapper" role="main"><div class="main-content"><noscript><div class="h2"><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script nonce="qtWhzRLUVA8OKImNpZbJOm">(function(){window._cf_chl_opt = {cFPWv: 'b',cH: 'o73X9zLPuiptmMu2AdOs8vknckZUDw4JfKHxc_..gpk-1781778996-1.2.1.1-EwQWGis8lmvzLdGgaFiBL65sZ0LlLOpF1.WdSrsQXHiVk8jO9MfNXogZ816rby2h',cITimeS: '1781778996',cN: 'qtWhzRLUVA8OKImNpZbJOm',cRay: 'a0d9a76a0a6446cc',cTplB: '0',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/2/tweets?__cf_chl_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA",cvId: '3',cZone: 'api.twitter.com',fa:"/2/tweets?__cf_chl_f_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA",md: 'xOZaFMM3FmH.UnwlAn2hQ10xhwN6hMZab3w8SuYLTYE-1781778996-1.2.1.1-GoidsXkPU8dbLazlrhl.CZnZwDnvUCySgAJoAiKxsN6Z5Mg5q0AkuwkMJz.PaHd2CYMjNuy1K8I_LVp9FuzEX9cE2fXY7Xr8qGBQAKiG_O83cR8kJQU5JHq6wA556zhclZIOIVU_6M0LT_mTu1Xdhmhs3LDkm4GeNXgG.CguF0qv6t.RuO8N2k9IPeBjMKj4wYoDhRJHiBaJz8pwkyKw.pvlxsO4eSZmwWPvQt3C92w2DzpjyefbYiGZU0FseXIXxuevXYUks6i4KL2HSSIoXhKQwVxftQegHMsXj6QkJ3cPILTRxsyPu8GELjxJtTRQz9J_JHStBqnvmBNA0Eg62blK0dGlSkvYWIsksElv49z14o_CjVfCqf0mj..DfrExC.wmRFsBNvgW3NWKcmf_osow0ViOU2W4zEO9BWmtiSDTAkElrv7qq9qmjFEi5Y1xKP3xtjKa52C.5z1WxChUG1T_1sJhwuuiE6B5f.m1vr3yU0M8gwkbor8L9KgBfMPybI5asfjylQrXAHyGe8kbOo4YtRlHM5XU4xgK3wKpzEbBN09jrYoOT0QCIVLzWjFOzOYKubmA3CwGUvoATGNx7tEF9cn_FNSmgNC01tCcue1Hz4LTgWk49XIE4_BhSB40fipNG1GxF8VIvJO3o.C86RLOJOMPsOcx.zVocLObZJXN.l.zdvyqAfvaLmVvd3165insTF_48FUkfudVid_AibeDix1XpDOIALNY7oQWDh5SXsd.s4CXisi0RpdpC3XQohjvP1EMNTrR3KslPzT5j9cMqxxxVplqXZH8qmy7TebVJGSvKsT2lmjadQJ2FNFLHxuN7giATE04rBoFs0NqVpZTjGK.2jIybfStptBf5uWFh1wzE6UdKV5CIvDPGC.9XhJGVeurqrEXVsc2b4eTEfzKrjbqNxTIW7qBNpHKuNv2ykx329IgN5VLjSeahtEgkyGIy5.RptcHkYSrM9f.wg',mdrd: '',};var a = document.createElement('script');a.nonce = 'qtWhzRLUVA8OKImNpZbJOm';a.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=a0d9a76a0a6446cc';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/2/tweets?__cf_chl_rt_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());</script></body></html>

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

❌ CRITICAL SYSTEM ERROR: 403 Forbidden

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[END]

====================================================

✅ WORKFLOW COMPLETED

====================================================Run python Auto_Post_Moonchill.py

python Auto_Post_Moonchill.py

shell: /usr/bin/bash -e {0}

env:

pythonLocation: /opt/hostedtoolcache/Python/3.9.25/x64

PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib/pkgconfig

Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.9.25/x64

LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.9.25/x64/lib

PYTHONUNBUFFERED: 1

CONSUMER_KEY: ***

CONSUMER_SECRET: ***

X_ACCESS_TOKEN: ***

X_ACCESS_TOKEN_SECRET: ***

เริ่มรันโหมดตรวจสอบระบบแบบ Full-Suite สำหรับ MoonChill (Auto Mode)...

============================================================

🛸 X API FULL-SUITE DIAGNOSTIC MODE

============================================================

[1] ENV VARIABLES CHECK

➤ CONSUMER_KEY : ✅ FOUND

➤ CONSUMER_SECRET : ✅ FOUND

➤ X_ACCESS_TOKEN : ✅ FOUND

➤ X_ACCESS_TOKEN_SECRET: ✅ FOUND

[2] AUTHENTICATION TEST (OAuth 1.0a)

❌ verify_credentials() FAILED

➤ Type : <class 'tweepy.errors.Forbidden'>

➤ Error : Forbidden('403 Forbidden')

➤ STATUS: 403 | BODY: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-1pwIhbiKKWngW3ym8RGxiR&#39; &#39;unsafe-eval&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) connect-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) frame-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; child-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+");background-repeat:no-repeat;background-size:contain;padding-left:34px}</style><meta http-equiv="refresh" content="360"></head><body><div class="main-wrapper" role="main"><div class="main-content"><noscript><div class="h2"><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script nonce="1pwIhbiKKWngW3ym8RGxiR">(function(){window._cf_chl_opt = {cFPWv: 'b',cH: '61wWMVaNTB6NnwZiGVn_MV9V_c_7dqWlBPg7MV.Ef2g-1781778976-1.2.1.1-xmtMIh5eDJd4MWoDED9W2wJ1jXdXucV4KeIqbEHZvN9uq013MJ3SiYHiAIuYXFss',cITimeS: '1781778976',cN: '1pwIhbiKKWngW3ym8RGxiR',cRay: 'a0d9a6ec3dbef084',cTplB: '0',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/1.1/account/verify_credentials.json?__cf_chl_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU",cvId: '3',cZone: 'api.twitter.com',fa:"/1.1/account/verify_credentials.json?__cf_chl_f_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU",md: '4An5Ylyuva9m5J5H_Cs1N8yZnctTdQ71g5353UHfDew-1781778976-1.2.1.1-2nmBs1RXWz8pcX.BB8XBxRXwDbjv1Pr8yQrprgoCZJBy__hT.sIaLusjRLqwbzNwde6sy8k9GD3gzAutPTAJ_SpVhh4sP.twfZNbH9qaeM.0VWmumvPEeeS1harQqTKINXsJrlGxyV47fLoZD7QDKKF.QtybcrKWCASGTglpcbf2xulf4o_0YXOpq0mKe2phXRBlEKZKNV4OnBkBLwhHBm23XVITf37fSU8LQL_E3UPduajFPjjdnV0q1YbKNnxMss7s2v7oo3ozEOx7nqQ2aULa3HtDdoaBmWLD1vEq6p._6FvCr1xWKGFXvPkZ9kMKvpIbK9Ir.e6duJDQBNhBB6eEb6IkkX9122UcUqbXNBueVLshE3eRXwNbZicgdbuL2X.RCQLfzTk5_jc7uFKb3XpLATBQnDrZsWIfPXtGnStxeAQ.ETk9XAXOzkrlLywTTa_cWNvXdhcIUxKKNfSPvg0vwHuc_JhxmLXxJVRfuXSfECwFA2uiBiqiCPwVWyfV9QDueK86MGDn6p2O2dbt0wdcYUB9UsOKJIH_bQSSla68N62Pc7fDPLGj0_bWLAQXfO0b0e2GLd3.c6Cll9Ga6nKClDjEGUjpnNoW1H_tsQDshqi4_RAJ6LOqj1BxFJJZWHQFw7YDgVIX1RtX_dHGA3UdhUcxh0pbPn9LR3PiOokV3alAy1nDxmLNXaOu34V4zmyYbbIY0hwOKRjdIQyBRIteg5iRJiIyd.LpCqHXt.B2MIN.l.oH4o5K50z6smIY4pQbwfdtSiS0Y7py3E06uVQSYqustxbf9XirrowtYuBXX5PqjGk3MCg7cJiD2.uSByIyPQoMo5mln5UvbttNJJI7LgbpC9ZNBcIDBQ8YS.qqBs2lpC0JaLyj5U9Edu7dLmqo8G6oX12nXM6k2_edA2cRwYHn0jMx_yr3S3liGnPh_d5pisWdnPhKOg6XU0TET1JKZSCkL8JrcjNf3eQaPbj4WlwzPctJK5bjBWYiwlFXiq6.7C5qthHubboz8b_N',mdrd: '',};var a = document.createElement('script');a.nonce = '1pwIhbiKKWngW3ym8RGxiR';a.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=a0d9a6ec3dbef084';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/1.1/account/verify_credentials.json?__cf_chl_rt_tk=yPLsWSchKQ7opVfLczFDm7s_iaucJdLhCS2l6TE79GE-1781778976-1.0.1.1-d2F07s_Tvg4i8A3kvGlzbscHpqb9Oc8rQq910ZIlFcU"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());</script></body></html>

╔════════════════════════════════════════════════════╗

║ d[o_0]b MOONCHILL X-BOT ║

╚════════════════════════════════════════════════════╝

⚙️ [SYSTEM CHECK]

====================================================

➤ Time Zone : Asia/Bangkok (UTC+7)

➤ Current Date : 2026-06-18

➤ Current Time : 17:36:16

➤ Context : Evening Round

➤ Target Time : 17:00

➤ Image : No

➤ Msg Loaded : 3 items

➤ Tag Pool : 14 tags

➤ Max Delay : 90 mins

====================================================

⏱︎ [WAITING PROCESS] [1/4]

====================================================

====================================================

[EXECUTION START] [2/4]

====================================================

📊 [TIME BUDGET ANALYSIS]

➤ Total Runtime : 110 mins

➤ Time Elapsed : 0.0 mins

➤ Remaining : 110.0 mins

➤ Config: 90m -> Safe: 90m (OK)

--------------------------------------------------

➤ Strategy : Random Delay (1m 20s)

... (Sleeping) ...

▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 10% | ETA: 00:00:18 | Sleeping...

▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 20% | ETA: 00:00:16 | Sleeping...

▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 30% | ETA: 00:00:14 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯ 40% | ETA: 00:00:12 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯▯▯▯ 50% | ETA: 00:00:10 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯▯▯ 60% | ETA: 00:00:08 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯▯▯▯ 70% | ETA: 00:00:06 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯▯▯ 80% | ETA: 00:00:04 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▯▯▯ 90% | ETA: 00:00:02 | Sleeping...

▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ 100% | ETA: 00:00:00 | Waking Up!

====================================================

[UPLOADING] [3/4]

====================================================

====================================================

[POSE] [4/4]

====================================================

❌ [TWITTER API ERROR]

➤ Type : <class 'tweepy.errors.Forbidden'>

➤ Error : Forbidden('403 Forbidden')

➤ STATUS: 403

➤ BODY : <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-qtWhzRLUVA8OKImNpZbJOm&#39; &#39;unsafe-eval&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) connect-src &#39;self&#39; [https://challenges.cloudflare.com;](https://challenges.cloudflare.com;) frame-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; child-src &#39;self&#39; [https://challenges.cloudflare.com](https://challenges.cloudflare.com) blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+");background-repeat:no-repeat;background-size:contain;padding-left:34px}</style><meta http-equiv="refresh" content="360"></head><body><div class="main-wrapper" role="main"><div class="main-content"><noscript><div class="h2"><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script nonce="qtWhzRLUVA8OKImNpZbJOm">(function(){window._cf_chl_opt = {cFPWv: 'b',cH: 'o73X9zLPuiptmMu2AdOs8vknckZUDw4JfKHxc_..gpk-1781778996-1.2.1.1-EwQWGis8lmvzLdGgaFiBL65sZ0LlLOpF1.WdSrsQXHiVk8jO9MfNXogZ816rby2h',cITimeS: '1781778996',cN: 'qtWhzRLUVA8OKImNpZbJOm',cRay: 'a0d9a76a0a6446cc',cTplB: '0',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/2/tweets?__cf_chl_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA",cvId: '3',cZone: 'api.twitter.com',fa:"/2/tweets?__cf_chl_f_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA",md: 'xOZaFMM3FmH.UnwlAn2hQ10xhwN6hMZab3w8SuYLTYE-1781778996-1.2.1.1-GoidsXkPU8dbLazlrhl.CZnZwDnvUCySgAJoAiKxsN6Z5Mg5q0AkuwkMJz.PaHd2CYMjNuy1K8I_LVp9FuzEX9cE2fXY7Xr8qGBQAKiG_O83cR8kJQU5JHq6wA556zhclZIOIVU_6M0LT_mTu1Xdhmhs3LDkm4GeNXgG.CguF0qv6t.RuO8N2k9IPeBjMKj4wYoDhRJHiBaJz8pwkyKw.pvlxsO4eSZmwWPvQt3C92w2DzpjyefbYiGZU0FseXIXxuevXYUks6i4KL2HSSIoXhKQwVxftQegHMsXj6QkJ3cPILTRxsyPu8GELjxJtTRQz9J_JHStBqnvmBNA0Eg62blK0dGlSkvYWIsksElv49z14o_CjVfCqf0mj..DfrExC.wmRFsBNvgW3NWKcmf_osow0ViOU2W4zEO9BWmtiSDTAkElrv7qq9qmjFEi5Y1xKP3xtjKa52C.5z1WxChUG1T_1sJhwuuiE6B5f.m1vr3yU0M8gwkbor8L9KgBfMPybI5asfjylQrXAHyGe8kbOo4YtRlHM5XU4xgK3wKpzEbBN09jrYoOT0QCIVLzWjFOzOYKubmA3CwGUvoATGNx7tEF9cn_FNSmgNC01tCcue1Hz4LTgWk49XIE4_BhSB40fipNG1GxF8VIvJO3o.C86RLOJOMPsOcx.zVocLObZJXN.l.zdvyqAfvaLmVvd3165insTF_48FUkfudVid_AibeDix1XpDOIALNY7oQWDh5SXsd.s4CXisi0RpdpC3XQohjvP1EMNTrR3KslPzT5j9cMqxxxVplqXZH8qmy7TebVJGSvKsT2lmjadQJ2FNFLHxuN7giATE04rBoFs0NqVpZTjGK.2jIybfStptBf5uWFh1wzE6UdKV5CIvDPGC.9XhJGVeurqrEXVsc2b4eTEfzKrjbqNxTIW7qBNpHKuNv2ykx329IgN5VLjSeahtEgkyGIy5.RptcHkYSrM9f.wg',mdrd: '',};var a = document.createElement('script');a.nonce = 'qtWhzRLUVA8OKImNpZbJOm';a.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=a0d9a76a0a6446cc';window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;if (window.history && window.history.replaceState) {var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;history.replaceState(null, null,"/2/tweets?__cf_chl_rt_tk=EQWVLy.qqvbovEl6VfU047tCKXTSDclycvQm2GjYEmM-1781778996-1.0.1.1-ai4TTyWF23t4jeYZJiW8B0iDwBOuYmgGCXAskF319CA"+ window._cf_chl_opt.cOgUHash);a.onload = function() {history.replaceState(null, null, ogU);}}document.getElementsByTagName('head')[0].appendChild(a);}());</script></body></html>

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

❌ CRITICAL SYSTEM ERROR: 403 Forbidden

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[END]

====================================================

✅ WORKFLOW COMPLETED

====================================================]