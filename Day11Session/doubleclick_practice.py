import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
doubleclick_ele=driver.find_element(by=By.XPATH,value="//button[text()=' Double click Here   ']")
act=ActionChains(driver)
act.double_click(doubleclick_ele).perform()
time.sleep(3)
alret_text=driver.switch_to.alert
print(alret_text.text)
alret_text.accept()
driver.close()