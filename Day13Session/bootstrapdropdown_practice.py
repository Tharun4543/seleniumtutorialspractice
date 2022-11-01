#Hands on with bootstrap dropdown
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/bootstrap-dropdown-example-for-selenium.html")
driver.find_element(by=By.XPATH,value="//button[@id='menu1']").click()
courses_list=driver.find_elements(by=By.XPATH,value="//li[@role='presentation']")
#print(len(courses_list))
for course in courses_list:
    if course.text=="JavaScript":
        course.click()
time.sleep(3)
driver.close()