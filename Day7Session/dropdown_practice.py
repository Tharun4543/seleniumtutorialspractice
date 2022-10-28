import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en/register?returnUrl=%2Fen%2Fget-started")
dropdown_options=Select(driver.find_element(by=By.XPATH,value="//select[@id='CountryId']"))
#Built in methods using selenium method
'''dropdown_options.select_by_visible_text("Cambodia")
dropdown_options.select_by_value("247")
dropdown_options.select_by_index(7)'''
#TO get all the drownvalues using options method
'''ddoptions_list=dropdown_options.options
print(len(ddoptions_list))
for option in ddoptions_list:
    print(option.text)'''

#How to select a dropdown value manually
'''ddoptions_list=dropdown_options.options
for option in ddoptions_list:
    if option.text=="India":
        option.click()
time.sleep(7)
driver.close()'''