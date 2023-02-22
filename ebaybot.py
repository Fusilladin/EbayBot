import time
import re
from datetime import datetime
import requests
import json
import csv
import os
import random 
from bs4 import BeautifulSoup as bs
import pypyodbc as odbc
from lxml import html
import requests_html
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

# db = 
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = '127.0.0.1'
DATABASE_NAME = 'EbayBot'

# uid=<username>;
# pwd=<password>;
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
conn = odbc.connect(connection_string)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
}

mycursor = conn.cursor

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("C:\\Users\\userTK427\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 13")

driver = uc.Chrome(chrome_options=chrome_options)
achains = ActionChains(driver)


# insert_query = '''
#         INSERT INTO dbo.test (id,first_name,last_name) 
#         VALUES (?,?,?);
# '''
# test_names = [[1,'Jack','Smith'],
#             [2,'Jill','Stanford']
#     ]
# for row in test_names:
#     values = (row[0],row[1],row[2])
#     cursor.execute(insert_query,values)
# conn.commit()

# cursor.execute("""SELECT *
#                 FROM dbo.test 
#                 """)

# for row in cursor:
#     print(row)

# /

# box listing page

urls = ["https://www.bulq.com/lots/?category=Computers%20%26%20Office"
    ,"https://www.bulq.com/lots/?category=Consumer%20Electronics"
    ,"https://www.bulq.com/lots/?category=Home%20%26%20Garden"
]


# boxes page
bulq_boxes = {
     "id" : []
    ,"name" : []
    ,"price" : []
    ,"category" : [] 
    ,"url" : []
    ,"shipping_included" : []
    ,"website" : [] # manual
    ,"retail_price" : []

}


def request():
    page = requests.get(url)
    content = html.fromstring(page.content)
    return content

def parse():
    content = request()
    containers = content.xpath(XPATHS[0])
    for container in containers:
        href = container.xpath(XPATHS[1])
        shipping_status = container.xpath(XPATHS[2])
        cost = container.xpath(XPATHS[3])
        id = container.xpath(XPATHS[4]) 
        item_name = container.xpath(XPATHS[5])
        retail_name = container.xpath(XPATHS[6])
        category = container.xpath(XPATHS[7])

        print(href,shipping_status,cost,id,item_name,retail_name,category)

XPATHS = ['//div[@class="col-lg-3 col-sm-4 col-xs-12 listing-square ng-scope ng-isolate-scope"]'
    ,'.//a[@class="ng-isolate-scope"]/a/@href'
    ,'.//a[@class="ng-binding"]/span/@class'
    ,'.//a[@class="ng-binding ng-hide"]/span/@class'
    ,'.//div[@class="listing-square__name ng-binding"]/div/@ng-bind'
    ,'.//div[@class="listing-title ng-binding"]/div/@class'
    ,'.//span[@class="ng-binding"]/span/@class'
    ,'//span[@class="results-header__category ng-binding"]/span/@ng-show'
    ]  

for url in urls:
    driver.get("https://bot.sannysoft.com/")
    time.sleep(1)

    elem_list = driver.find_element(By.XPATH,XPATHS[0])    
    items = "".join(str(elem_list.text)).split("\n")
    print(items[0])
    time.sleep(30)




# box inventory page
'''
# box_id
# REMOVE CATEGORY
products = {
     "title" : []
    ,"price" : []
    ,"quantity" : []
    ,"category" : []
    ,"upc" : [] 
}

r = requests.get(url,headers=headers)
soup = str(bs(r.text,features='lxml'))
data1 = re.compile('(?<="qty":\[){"upc":"(.+)')
matches = str(data1.findall(soup))
# print(soup)

data2 = re.compile('(?<="title":")(\w|\s|\d|\/|\-|\.)+')
titles = data2.finditer(matches)
for title in titles:
    x = title.group()
    products['title'].append(x)

data2 = re.compile('(?<="msrp_cents":)\d+')
prices = data2.finditer(matches)
for price in prices:
    x = str(price.group())
    y = len(x)-2
    x = x[0:-2] + "." + x[y:]
    products['price'].append(x)

data2 = re.compile('(?<="quantity":)\d+')
quantities = data2.finditer(matches)
for quantity in quantities:
    x = str(quantity.group())
    products['quantity'].append(x)

data2 = re.compile('(?<="category":")\w+')
categories = data2.finditer(matches)
for category in categories:
    x = str(category.group())
    products['category'].append(x)

data2 = re.compile('\d+(?=","title)')
upcs = data2.finditer(matches)
for upc in upcs:
    x = str(upc.group())
    products['upc'].append(x)

print(products)

url = "https://www.ebay.com/sch/i.html?_nkw=195553202824&_trksid=m5467.l1311"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
}
ebay_products = {
     "title" : []
    ,"price" : []
    ,"row_number" : []
}


'''




