#Hands on implicitly_wait
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com/")
searchbar_value=driver.find_element(by=By.XPATH,value="//input[@title='Search']")
searchbar_value.send_keys("Selenium using python")
searchbar_value.submit()
searched_webpage=driver.find_element(by=By.XPATH,value="//h3[contains(text(),'Selenium WebDriver with Python Tutorial - Javatpoi')]")
searched_webpage.click()
time.sleep(5)
driver.close()
