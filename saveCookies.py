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
import time
import pickle

chrome_options = uc.ChromeOptions()
driver = uc.Chrome(chrome_options=chrome_options)
achains = ActionChains(driver)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
}
driver.get("https://www.bulq.com/")
time.sleep(1)
cookies = driver.get_cookies()
print(cookies)
pickle.dump(cookies, open("cookies.pkl","wb"))


