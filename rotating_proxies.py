import requests

# url = "https://httpbin.org/ip"
url = "https://ipinfo.io/json"

proxies = {
    "http" :"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_skipispstatic-1@geo.iproyal.com:12321"
    ,"https":"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_skipispstatic-1@geo.iproyal.com:12321"
}

r = requests.get(url,proxies=proxies)
# print(r.json()['ip'])
print(r.text)