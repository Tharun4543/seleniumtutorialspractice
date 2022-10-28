#Hands on with Iframes or frames
import time

import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.switch_to.frame("frm1")
iframe_path=driver.find_element(by=By.ID,value="selectnav2")
dropdown_options=Select(iframe_path)
dropdown_list=dropdown_options.options
for option in dropdown_list:
    if option.text=="Contact":
        option.click()
time.sleep(3)
print(len(dropdown_list))
driver.close()
