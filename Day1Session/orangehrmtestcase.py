import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
s=Service("C://Users//ntharun//Downloads//chromedriver_win32 (2)//chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get('https://github.com/login')
driver.find_element(by=By.ID,value="login_field").send_keys("nagiritharun4543@gmail.com")
driver.find_element(by=By.ID,value="password").send_keys("Chinna@6304")
driver.find_element(by=By.NAME,value="commit").click()
time.sleep(30)
driver.close()