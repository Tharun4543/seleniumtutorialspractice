#hands on with upload a file in a webapplication
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.execute_script("window.scrollBy(0,1500)"," ")
driver.find_element(by=By.XPATH,value="//input[@id='uploadfile']").send_keys("C:\\PERSONALFOLDERS\\PERSONALFILES\\NTRESUME.docx")
time.sleep(5)
driver.close()