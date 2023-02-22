import requests
import pandas as pd
from playwright.sync_api import sync_playwright

PROXIES = {
    "http" :"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_skipispstatic-1@geo.iproyal.com:12321"
    ,"https":"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_skipispstatic-1@geo.iproyal.com:12321"
}

def get_cookie_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(f"https://www.bulq.com/lots/search/?category=Computers%20%26%20Office&lot_size%5B%5D=Case&sort_direction=desc&sort_field=updated_at")
        # page.click("button")
        # resp
        # print
        # print(context.cookies())
        cookie_for_requests = context.cookies()[0]['value']
        # print(cookie_for_requests)
        browser.close()
    return cookie_for_requests

def req_with_cookie(cookie_for_requests):
    cookies = dict(
        Cookie=f'INGRESSCOOKIE={cookie_for_requests}^|44e369bec5910462e5c64de38aeff9d8; _mibhv=anon-1671746965452-9626720393_6782; pxcts=4cbebca3-8245-11ed-928d-4442524e7157; _pxvid=4c870f3b-8245-11ed-a623-506f436f5051; _gid=GA1.2.1939206997.1671746966; _fbp=fb.1.1671746966247.1798139401; ln_or=eyI2MzQ5NjIiOiJkIn0^%^3D; __attentive_id=92eb651c2c0b4ac68164536412cd8540; __attentive_cco=1671746966404; _attn_=eyJ1Ijoie1wiY29cIjoxNjcxNzQ2OTY2NDE0LFwidW9cIjoxNjcxNzQ2OTY2NDE0LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjkyZWI2NTFjMmMwYjRhYzY4MTY0NTM2NDEyY2Q4NTQwXCJ9In0=; __qca=P0-528944077-1671746966207; __attentive_dv=1; __zlcmid=1DYlTCfHTSbwfHB; tpc_a=5f6d71034d4448eb9d145bf7bb638b26.1671746966.LRs.1671764903; _uetsid=4c3bd770824511eda65a23685a0b42e0; _uetvid=4c3c1fb0824511ed84451dc6d207b268; _ga=GA1.1.725119518.1671746966; _session_id=eabccaea6d308e9d19380228ea8ac0a7; _ga_33STNEKCQH=GS1.1.1671830960.4.0.1671830960.0.0.0; forterToken=7033463fa49948afa7ce4c84c44209b7_1671830961525__UDF43_13ck; bulq_cart=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxMD0iLCJleHAiOiIyMDIzLTAxLTIyVDIxOjI5OjIyLjc5MVoiLCJwdXIiOm51bGx9fQ^%^3D^%^3D--538a9caf3ac27c5716445addf42352644b68f334; _pxhd=y6dC-VNpAu8nfyrn0l5/5uaI85oMu1B1uNQ2HyXX2/pD-ASEPvvhVIcsAQZApkR6suxxFqHEQwZlEEpgWNpz/w==:hDB2sS5kZTV277-a4SyAZ8/B/nQtrNk9eOMbzh55WZtqRuUHsygVWqM4Mgj1c54I1ipnuKuLhRKdXjca5MK3OjDrOYajbWUldnmaqwg2JO0=; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _px2=eyJ1IjoiZGQ2NDUyZjAtODMwOC0xMWVkLWIzZTctZjMzYzliMjU0MmQxIiwidiI6IjcxYjg5YTBhLTgyNjUtMTFlZC1hYmNjLTYxNzE1YTY2NTc2NyIsInQiOjE2NzE4MzEyNjI2NDEsImgiOiIxOTUyODFlMTg5ZDc5YTYxZGUyZGI2Yjc4MzBhZmI0YWM1MzU1MmExOWQ2MTUyMGZlYzc1NTdiZjAyNzkwNTg2In0='
    )
    url = "https://www.bulq.com/api/listings"
    page_num = 0
    for page_num in range(0,2):
        querystring = {"category":"Computers^%^20^%^26^%^20Office","sort_direction":"desc","sort_field":"updated_at","page":f"{page_num}"}

        payload = ""
        headers = {
            "cookie": f"bulq_cart=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxMD0iLCJleHAiOiIyMDIzLTAxLTIyVDIzOjIwOjE2LjkzNloiLCJwdXIiOm51bGx9fQ%253D%253D--b1bf6af173a4be9c929009e551e817d27d611c13; _session_id=02a2527a2fe8d049df2a9a0f00e9a833; _pxhd=vqyJXaeHQ91qFa2h6P93Y8lT0YP5NF6%2FdsnfOWiPn-UvUr1WdeYXiYrv9l0xYNrn1GQKunNyHU7eDbhVMZD4Og%3D%3D%3A8rxr-K6Gp4JatrqxmXhEbD-NYu6TjsaRHCBEPAipraOi9jmwv8-j3H-nKjzUbIU%2F-Hq91s2ZX2BsNkf8s-bdf3EAn4WGdZwQzrN%2F1ENHWSc%3D",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "ApiVersion": "5",
            "Connection": "keep-alive",
            "Cookie": f"INGRESSCOOKIE={cookie_for_requests}^|44e369bec5910462e5c64de38aeff9d8; _mibhv=anon-1671746965452-9626720393_6782; pxcts=4cbebca3-8245-11ed-928d-4442524e7157; _pxvid=4c870f3b-8245-11ed-a623-506f436f5051; _gid=GA1.2.1939206997.1671746966; _fbp=fb.1.1671746966247.1798139401; ln_or=eyI2MzQ5NjIiOiJkIn0^%^3D; __attentive_id=92eb651c2c0b4ac68164536412cd8540; __attentive_cco=1671746966404; _attn_=eyJ1Ijoie1wiY29cIjoxNjcxNzQ2OTY2NDE0LFwidW9cIjoxNjcxNzQ2OTY2NDE0LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjkyZWI2NTFjMmMwYjRhYzY4MTY0NTM2NDEyY2Q4NTQwXCJ9In0=; __qca=P0-528944077-1671746966207; __attentive_dv=1; __zlcmid=1DYlTCfHTSbwfHB; tpc_a=5f6d71034d4448eb9d145bf7bb638b26.1671746966.LRs.1671764903; _uetsid=4c3bd770824511eda65a23685a0b42e0; _uetvid=4c3c1fb0824511ed84451dc6d207b268; _ga=GA1.1.725119518.1671746966; _session_id=eabccaea6d308e9d19380228ea8ac0a7; _ga_33STNEKCQH=GS1.1.1671830960.4.0.1671830960.0.0.0; forterToken=7033463fa49948afa7ce4c84c44209b7_1671830961525__UDF43_13ck; bulq_cart=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxMD0iLCJleHAiOiIyMDIzLTAxLTIyVDIxOjI5OjIyLjc5MVoiLCJwdXIiOm51bGx9fQ^%^3D^%^3D--538a9caf3ac27c5716445addf42352644b68f334; _pxhd=y6dC-VNpAu8nfyrn0l5/5uaI85oMu1B1uNQ2HyXX2/pD-ASEPvvhVIcsAQZApkR6suxxFqHEQwZlEEpgWNpz/w==:hDB2sS5kZTV277-a4SyAZ8/B/nQtrNk9eOMbzh55WZtqRuUHsygVWqM4Mgj1c54I1ipnuKuLhRKdXjca5MK3OjDrOYajbWUldnmaqwg2JO0=; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _px2=eyJ1IjoiZGQ2NDUyZjAtODMwOC0xMWVkLWIzZTctZjMzYzliMjU0MmQxIiwidiI6IjcxYjg5YTBhLTgyNjUtMTFlZC1hYmNjLTYxNzE1YTY2NTc2NyIsInQiOjE2NzE4MzEyNjI2NDEsImgiOiIxOTUyODFlMTg5ZDc5YTYxZGUyZGI2Yjc4MzBhZmI0YWM1MzU1MmExOWQ2MTUyMGZlYzc1NTdiZjAyNzkwNTg2In0=",
            "Referer": f"https://www.bulq.com/lots/search/?category=Computers^%^20^%^26^%^20Office&sort_direction=desc&sort_field=updated_at",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": f"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
            "X-CSRF-Token": f"2g9cA+AfnJKyNK28BoL4Dx4Qlbf45HCvGKPq9Xg/g+GVBc682xMvZWVPQetn7WztsUx17Qo6SlMBJxXzynUaCQ==",
            "sec-ch-ua": f"^\^Not?A_Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^108^^, ^\^Google",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "^\^Android^^"
        }

        r = requests.request("GET", url, data=payload, headers=headers, params=querystring,proxies=PROXIES)

        data = r.json()
        print(data)
        # quit()
req_with_cookie(get_cookie_playwright())
