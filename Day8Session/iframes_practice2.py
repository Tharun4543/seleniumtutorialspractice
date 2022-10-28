#Hands on with Iframes or frames
'''
    we can switch to frame in 4 ways.
    1.Using ID name
    2.Using Name name
    3.Using Index
    4.Using WebElement
'''
import time

import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://docs.oracle.com/javase/7/docs/api/")
#Switch to frame Using webELement
Identify_frame=driver.find_element(by=By.XPATH,value="//frame[@name='packageListFrame']")

driver.switch_to.frame(Identify_frame)
driver.find_element(by=By.XPATH,value="//a[.='java.awt.datatransfer']").click()
time.sleep(3)
driver.switch_to.default_content()
#Switch to frame using Name
driver.switch_to.frame("packageFrame")
driver.find_element(by=By.LINK_TEXT,value="StringSelection").click()
time.sleep(5)
#Switch to frame using Index
driver.switch_to.default_content()
driver.switch_to.frame(2)
driver.find_element(by=By.LINK_TEXT,value="Overview").click()
time.sleep(5)
driver.close()