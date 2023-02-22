import requests

proxies = {
    "http" :"http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}
requests.get("http://example.org", proxies=proxies)
# Rotating requests through a proxy pool
from lxml.html import fromstring

def get_proxies():
    url = "https://IPRoyal.com/"
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()

    for i in parser.xpath("//tbody/tr")[:10]:
        if i.xpath(".//td[7][contains(text(),”yes”)]"):
    #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath(".//td[1]/text()")[0], i.xpath(".//td[2]/text()")[0]])
            proxies.add(proxy)

