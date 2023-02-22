# from selenium import webdriver 
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
from seleniumwire import webdriver
import time
import pickle

# mycursor = conn.cursor
service = r'C:\\chromedriver.exe'

# chrome_options = uc.ChromeOptions()
options = {
    'proxy': {
        'http': 'http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:11111',
        'https': 'http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:11111',
    }
}
driver = webdriver.Chrome(executable_path=service,
                          seleniumwire_options=options)
achains = ActionChains(driver)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
}
# proxies = {
#     "http" :"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:12321"
#     ,"https":"http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:12321"
# }

urls = [f"https://www.bulq.com/lots/search/?category=Computers%20%26%20Office&sort_direction=desc&sort_field=updated_at"
    ,f"https://www.bulq.com/lots/search/?category=Consumer%20Electronics&sort_direction=desc&sort_field=updated_at"
    ,f"https://www.bulq.com/lots/search/?category=Home%20%26%20Garden&sort_direction=desc&sort_field=updated_at"
]

bulq_boxes = {
     "id" : []
    ,"name" : []
    ,"cost" : []
    ,"retail_price" : []
    ,"category" : [] 
    ,"box_url" : []
    ,"shipping" : []
    ,"main_website" : []
}
bulq_products = {
     "box_id" : []
    ,"title" : []
    ,"item_price" : []
    ,"quantity" : []
    ,"upc" : []
}

try:
    cookies = pickle.load(open("cookies.pkl","rb"))
    cookies = driver.get_cookies()
except Exception as e:
    print(e)
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl","wb"))

for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

time.sleep(3)
for url in urls:
    driver.get(url)
    elem_list = driver.find_elements(By.XPATH,'//div[@class="col-lg-3 col-sm-4 col-xs-12 listing-square ng-scope ng-isolate-scope"]')
    num=0
    category_element = (driver.find_element(By.XPATH,'//span[@class="results-header__category ng-binding"]')).text
    
    for elem in elem_list:
        getr_box_url_element = (driver.find_element(By.XPATH,'//a[@class="ng-isolate-scope"]'))
        box_url_element = getr_box_url_element.get_attribute('href')
        elem = "".join(str(elem.text)).split("\n")
        # print(elem)
        num+=1
        # print(num)
        if "Price Drop" not in elem[0]:
            if elem[8] == "+ Shipping":
                pass
            else:
                bulq_boxes['id'].append(elem[0])
                bulq_boxes['name'].append(elem[1])
                bulq_boxes['cost'].append(elem[7])
                bulq_boxes['shipping'].append(elem[8])
                bulq_boxes['retail_price'].append(elem[4])
                bulq_boxes['category'].append(category_element)
                bulq_boxes['main_website'].append(url)
                bulq_boxes['box_url'].append(box_url_element)
    print(bulq_boxes['box_url'])   
                
'''
                try:
                    achains.move_to_element(getr_box_url_element).key_down(Keys.SHIFT).click().key_up(Keys.CONTROL).perform()
                except Exception as e:
                    print(e)
                p = driver.current_window_handle
                parent = driver.window_handles[0]
                try:
                    chld = driver.window_handles[1]
                except Exception as e:
                    print(e)
                driver.switch_to.window(chld)
                 # driver.get(box_url_element)
                # box_id, title, item_price, quantity, upc
                time.sleep(5)
                # driver.close()
                # driver.switch_to.window(parent)
        
        else:
            if elem[9] == "+ Shipping": # box_url
                pass
            else:
                bulq_boxes['id'].append(elem[1])
                bulq_boxes['name'].append(elem[2])
                bulq_boxes['cost'].append("".join(str(elem[8])).split(" ")[0])
                bulq_boxes['shipping'].append(elem[9])
                bulq_boxes['retail_price'].append(elem[5])
                bulq_boxes['category'].append(category_element)
                bulq_boxes['main_website'].append(url)
                bulq_boxes['box_url'].append(box_url_element)
    print(bulq_boxes)
        

        time.sleep(1)
        items = elem.text #driver.find_element(By.XPATH,'//div[@class="col-lg-3 col-sm-4 col-xs-12 listing-square ng-scope ng-isolate-scope"]')    
        e = "".join(str(elem.text)).split("\n")
        items = e[14:100] # id[0],name[1],retail_price[4],cost[6],shipping[7]
        print(items)
        n = 0
        while True:
            try:
                shipping = items[(n+7)]
                if shipping == "Shipping Included":
                    bulq_boxes["shipping_included"].append(shipping)
                else:
                    continue
            except IndexError:
                pass

            bulq_boxes["id"].append(items[n])
            bulq_boxes["name"].append(items[(n+1)])
            bulq_boxes["cost"].append(items[(n+6)])
            bulq_boxes["retail_price"].append(items[(n+4)])
            bulq_boxes["category"].append(e[1])
            bulq_boxes["website"].append(url)

            e = driver.find_element(By.XPATH,'//span[@class="results-header__category ng-binding"]')
            e=driver.find_element(By.XPATH,'//a[@class="ng-isolate-scope"]')
            bulq_boxes["url"].append(e.get_attribute('href'))
            
            break
            print(bulq_boxes)

    
            time.sleep(120)
'''
