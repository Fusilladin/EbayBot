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
        Cookie=f'INGRESSCOOKIE={cookie_for_requests}'
    )
    url = "https://www.bulq.com/api/listings"
    page_num = 0
    for page_num in range(0,2):
        querystring = {"category":"Computers^%^20^%^26^%^20Office","sort_direction":"desc","sort_field":"updated_at","page":f"{page_num}"}

        payload = ""
        headers = {
            "cookie": f"",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "ApiVersion": "5",
            "Connection": "keep-alive",
            "Cookie": f"INGRESSCOOKIE={cookie_for_requests}",
            "Referer": f"https://www.bulq.com/lots/search/?category=Computers^%^20^%^26^%^20Office&sort_direction=desc&sort_field=updated_at",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": f"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
            "X-CSRF-Token": f"",
            "sec-ch-ua": f"^\^Not?A_Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^108^^, ^\^Google",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "^\^Android^^"
        }

        r = requests.request("GET", url, data=payload, headers=headers, params=querystring,proxies=PROXIES)

        data = r.json()
        print(data)
        # quit()
req_with_cookie(get_cookie_playwright())
