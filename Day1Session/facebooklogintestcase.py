'''
1.Launch Chrome browser
2.open facebook URL
3.Enter username and password
4.click on login
5.get the title
6.validate the title whether it is correct or not.
'''
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C://Users//ntharun//Downloads//chromedriver_win32 (2)//chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/login/")

driver.find_element(by=By.ID,value="email").send_keys("nagiritharun4543@gmail.com")
driver.find_element(by=By.ID,value="pass").send_keys("Chinna@6304")
driver.find_element(by=By.ID,value="loginbutton").click()
