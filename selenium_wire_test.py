from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

service = r'C:\\chromedriver.exe'
options = {
    'proxy': {
        'http': 'http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:12321',
        'https': 'http://oLh11tm3M2yRbTBGd8ZU3nxmyIM56:1gn2CVI8t04CD6up_country-us_skipispstatic-1@geo.iproyal.com:12321',
    }
}

driver = webdriver.Chrome(executable_path=service,
                          seleniumwire_options=options)
achains = ActionChains(driver)

driver.get(f"https://www.bulq.com/lots/?category=Computers%20%26%20Office")
time.sleep(1)
item = driver.find_element(By.XPATH,'//div[@class="col-lg-3 col-sm-4 col-xs-12 listing-square ng-scope ng-isolate-scope"]')
print(item.text)
time.sleep(1)

# try:
#     achains.move_to_element(item).key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()
# except Exception as e:
#     print(e)
# p = driver.current_window_handle
# parent = driver.window_handles[0]
# try:
#     chld = driver.window_handles[1]
# except Exception as e:
#     print(e)
# driver.switch_to.window(chld)
# time.sleep(10)
# driver.close()
# driver.switch_to.window(parent)
# time.sleep(10)

