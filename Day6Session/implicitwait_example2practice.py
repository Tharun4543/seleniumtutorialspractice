import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(by=By.XPATH,value="//button[text()='Dropdown']").click()
mywait=WebDriverWait(driver,timeout=20.0)
#dropdown=mywait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Flipkart")))

driver.find_element(By.LINK_TEXT,value="Flipkart").click()
driver.quit()


