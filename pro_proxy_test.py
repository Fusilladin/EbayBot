import requests
from bs4 import BeautifulSoup
import statistics

BASE_URL = "https://books.toscrape.com/"
url = BASE_URL + "catalogue/category/books/philosophy_7/index.html"

PROXIES = {
    "http" :"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:12321"
    ,"https":"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:12321"
}

# username, password = open('creds.txt','r').read().splitlines()

# def proxy_request(url):
#     payload = {
#          "source":"universal"
#         ,"url":url
#         ,"geo_location":"United States"
#     }
#     r = requests.request(
#          "POST", "https://realtime.oxylabs.io/v1/queries"
#         ,auth = (username,password)
#         ,json = payload
#     )
#     response_html = r.json()['results'][0]['content']
#     return BeautifulSoup(response_html,'lxml')
# soup = proxy_request(url)

r = requests.get(f"https://www.bulq.com/lots/?category=Computers%20%26%20Office",proxies=PROXIES)
soup = BeautifulSoup(r.text,parser="lxml")
print(soup.find_all('a'))



# price_tags = soup.find_all('p',{'class':'price_color'})
# prices = [(price.text) for price in price_tags]
# print(prices)
# print(statistics.mean(prices))

