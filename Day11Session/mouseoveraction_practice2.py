'''
Hands on with
  1.mouse over action

'''

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
driver.get("https://www.amazon.in/")
time.sleep(10)
selectlang_ele=driver.find_element(by=By.XPATH,value="//div[normalize-space()='EN']")
act=ActionChains(driver)
act.move_to_element(selectlang_ele).perform()
time.sleep(5)
driver.find_element(by=By.XPATH,value="//div[@id='nav-flyout-icp']//div[contains(@class,'icp-helplink')][normalize-space()='Learn more']").click()
time.sleep(5)


driver.close()