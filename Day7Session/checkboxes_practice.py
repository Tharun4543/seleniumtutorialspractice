'''Hands on with
     Checkboxes
     Dropdown box
     Hyperlinks

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select one checkbox among all the checkboxes.
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkbox_values=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")
driver.find_element(By.ID,value="friday").click()
time.sleep(5)
print(len(checkbox_values))
for value in checkbox_values:
    print(value.get_attribute("id"))
driver.close()


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select multiple checkboxes among all the checkboxes.
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkbox_values=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")

for checkbox in checkbox_values:
    if checkbox.get_attribute("id")=="monday" or checkbox.get_attribute("id")=="tuesday":
        checkbox.click()


time.sleep(5)
driver.close()'''

#Select all checkboxes at one shot.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select multiple checkboxes among all the checkboxes.
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkbox_values=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")
for checkbox in checkbox_values:
    checkbox.click()
time.sleep(5)
driver.close()
