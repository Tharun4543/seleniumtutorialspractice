import time
#import driver as driver
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.automationtesting.in/FileDownload.html")
time.sleep(5)
driver.find_element(by=By.LINK_TEXT,value="Download").click()



driver.close()
