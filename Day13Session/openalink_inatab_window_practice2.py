'''
    Hands on with
        1.Open a link in a new tab.
        2.Open a link in a new window.
'''
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
#Open a register link in a new tab
register_linkele=driver.find_element(by=By.XPATH,value="//a[@class='ico-register']")
control_clickbtn=Keys.CONTROL+Keys.RETURN
register_linkele.send_keys(control_clickbtn)
time.sleep(3)
login_linkele=driver.find_element(by=By.XPATH,value="//a[@class='ico-login']")
login_linkele.send_keys(control_clickbtn)
time.sleep(3)
driver.close()