#Demonstration of Text
#Example for with inner text(note:it does not throw any exception if inner text not there)
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
namefield=driver.find_element(by=By.ID,value="password")
nametext=namefield.text
print(nametext)
driver.close()

##Example for with inner text(note:it does not throw any exception if inner text not there)
# import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
namefield=driver.find_element(by=By.XPATH,value="//button[normalize-space()='Submit']")
nametext=namefield.text
print(nametext)
driver.close()
#get_attribute method
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
passwordvalue=driver.find_element(by=By.ID,value="password")
classvalue=passwordvalue.get_attribute("class")
print(classvalue)
driver.close()'''

#get_attribute method with does not have value
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
passwordvalue=driver.find_element(by=By.ID,value="password")
classvalue=passwordvalue.get_attribute("name")
print(classvalue)
driver.close()
