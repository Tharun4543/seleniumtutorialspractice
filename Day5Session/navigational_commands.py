#Hands on with navigational commands
'''
1.back()
2.forward()
3.refresh()
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.get("https://www.amazon.in/")
driver.get("https://www.snapdeal.com/")
driver.back()
driver.back()
driver.refresh()
driver.forward()
driver.forward()
driver.refresh()
driver.back()
driver.back()
driver.close()