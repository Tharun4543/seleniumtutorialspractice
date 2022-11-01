'''
    Hands on with
        1.Open a link in a new tab.
        2.Open a link in a new window.
'''
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en/login?returnUrl=%2Fen%2Fget-started")
profile_options=driver.find_element(by=By.XPATH,value="//span[@class='user-actions-ico']//*[name()='svg']")
actions=ActionChains(driver)
actions.move_to_element(profile_options).perform()
register_link=Keys.CONTROL+Keys.RETURN
time.sleep(5)
mywait=WebDriverWait(driver,12)
mywait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Register']")))
driver.find_element(by=By.XPATH,value="//span[normalize-space()='Register']").send_keys(register_link)
time.sleep(3)
driver.close()
