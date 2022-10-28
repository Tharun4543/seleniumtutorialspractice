#Hands on with checkboxes
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select last 2 checkboxes among all the checkboxes.
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkbox_values=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")
for checkbox in range(len(checkbox_values)-2,len(checkbox_values)):
    checkbox_values[checkbox].click()
time.sleep(5)
driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select last 2 checkboxes among all the checkboxes.
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkbox_values=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")
for checkbox in range(len(checkbox_values)):
    if checkbox<4:
        checkbox_values[checkbox].click()
time.sleep(5)
driver.close()'''
