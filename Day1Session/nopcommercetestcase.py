import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.find_element(by=By.ID,value="Email").send_keys("nagiritharun4543@gmail.com")
driver.find_element(by=By.ID,value="Password").send_keys("Deepar@22")
driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button").click()
time.sleep(10)
driver.close()