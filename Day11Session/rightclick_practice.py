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
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
rightclick_ele=driver.find_element(by=By.XPATH,value="//span[text()='right click me']")
act=ActionChains(driver)
act.context_click(rightclick_ele).perform()
edit_option=driver.find_element(by=By.XPATH,value="//span[text()='Edit']")
time.sleep(5)
edit_option.click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.close()


