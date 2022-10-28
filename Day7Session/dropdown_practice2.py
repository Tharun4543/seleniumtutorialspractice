import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
dropdown_options=driver.find_element(by=By.XPATH,value="//select[@id='drop1']")
dropdown_values=Select(dropdown_options)
dropdown_list=dropdown_values.options
print(len(dropdown_list))
for option in dropdown_list:
    if option.text=="doc 1":
        print(option.click())
time.sleep(5)

driver.close()











