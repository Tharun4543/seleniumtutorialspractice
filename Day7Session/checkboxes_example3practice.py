import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select last 2 checkboxes among all the checkboxes.
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#select one field in all checkboxes
checkboxlist=driver.find_elements(By.XPATH,value="//label[normalize-space()='Which automation tools/frameworks do you use?']//following-sibling::div")
print(len(checkboxlist))
for checkbox in checkboxlist:
        checkbox.click()
time.sleep(10)
driver.close()

