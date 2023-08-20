import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH, value="//select[@id='searchDropdownBox']").click()
time.sleep(1000)
