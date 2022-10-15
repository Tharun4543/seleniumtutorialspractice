#hands on with conditional commands(Returns True or False)
'''
is_displayed(to know whether the attribute is present or not in the application)
is_enabled(to know whether the attribute takes input in the application)
is-selected(this method suitable for radio buttons and checkboxes)
'''
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
status_of_field=driver.find_element(by=By.XPATH,value="//input[@id='email']").is_displayed()
status_of_nfield=driver.find_element(by=By.XPATH,value="//input[@id='email']").is_enabled()
print(status_of_field)
print(status_of_nfield)
driver.close()'''

#isselected method
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/login")
driver.find_element(by=By.XPATH,value="//a[.='Sign up for Facebook']").click()
'''status_of_frbutton=driver.find_element(by=By.XPATH,value="//label[text()='Female']").is_selected()
status_of_mrbutton=driver.find_element(by=By.XPATH,value="//label[text()='Male']").is_selected()
status_of_csbutton=driver.find_element(by=By.XPATH,value="//label[text()='Custom']").is_selected()'''
fradiobutton=driver.find_element(by=By.XPATH,value="//label[text()='Female']")
fradiobutton.click()
time.sleep(10)
#the below status is After selecting the female radio button
status_of_frbutton=fradiobutton.is_selected()
print(status_of_frbutton)
'''status_of_mrbutton=driver.find_element(by=By.XPATH,value="//label[text()='Male']").is_selected()
status_of_csbutton=driver.find_element(by=By.XPATH,value="//label[text()='Custom']").is_selected()
print(status_of_frbutton)
print(status_of_mrbutton)
print(status_of_csbutton)
print("the below status is After selecting the female radio button")
print(status_of_frbutton)
print(status_of_mrbutton)
print(status_of_csbutton)'''
driver.close()
