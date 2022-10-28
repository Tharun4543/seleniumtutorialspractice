'''
Hands on with
  1.mouse over action

'''

'''import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/?ref_=nav_signin")
account_name=driver.find_element(by=By.XPATH,value="//span[@id='nav-link-accountList-nav-line-1']")
actions_object=ActionChains(driver)
actions_object.move_to_element(account_name).perform()
wish_websitelink=driver.find_element(by=By.XPATH,value="//span[text()='Wish from Any Website']")
wish_websitelink.click()
print(driver.title)
time.sleep(3)
driver.close()'''

#Example 2:
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
driver.get("https://www.amazon.in/?ref_=nav_signin")
language_options=driver.find_element(by=By.XPATH,value="//span[@class='icp-nav-link-inner']")
action_object=ActionChains(driver)
action_object.move_to_element(language_options).perform()
time.sleep(5)
help_link=driver.find_element(by=By.XPATH,value="//div[@id='nav-flyout-icp']//div[contains(@class,'icp-mkt-change-lnk')]")
help_link.click()
print(driver.title)
driver.close()