import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
#Select checkbox among all the checkboxes.
driver.get("https://demo.guru99.com/test/radio.html")
checkbox_list=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox']")
#print the value of the checkboxes.
'''for checkbox in checkbox_list:
    print(checkbox.get_attribute("value"))
driver.close()'''
#select one checkbox among all the checkboxes.
'''driver.find_element(by=By.XPATH,value="//input[@value='checkbox2']").click()
time.sleep(5)
driver.close()'''
#select multiple checkboxes among all the checkboxes.
'''for checkbox in checkbox_list:
    if checkbox.get_attribute("value")=="checkbox2" or checkbox.get_attribute("value")=="checkbox3":
        checkbox.click()
time.sleep(5)
driver.close()'''
#select all the checkboxes at one shot.
for checkbox in checkbox_list:
    checkbox.click()
time.sleep(5)
driver.close()