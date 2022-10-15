import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(by=By.ID,value="user-name").send_keys("standard_user")
driver.find_element(by=By.ID,value="password").send_keys("secret_sauce")
driver.find_element(by=By.ID,value="login-button").click()
time.sleep(20)
driver.close()