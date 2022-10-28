import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")
deadlinks_list=driver.find_elements(by=By.XPATH,value="//a")
try:
    for link in deadlinks_list:
        url=link.get_attribute("href")
        res=requests.head(url)
        if res.status_code>400:
            print(url,"Dead link")
        else:
            print("hyper link")
except:
    print("exception handeled")
driver.close()