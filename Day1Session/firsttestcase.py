'''open chrome browser
2.launch orangehrm url
3.enter username and password
4.click on login button
5.validate the titile of the page whether it is correctly displayed or not

from selenium import webdriver
from selenium.webdriver.common import by

driver=webdriver.Chrome("C://Users//ntharun//Downloads//chromedriver_win32 (2)//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(by.NAME,"username").send_keys("Admin")
driver.find_element(by.NAME,"password").send_keys("admin123")
driver.find_element(by.TYPE,"submit").click()
title1=driver.title
exceptedtitle="OrangeHRM"
if title1==exceptedtitle:
    print("Title is matched")
else:
    print("Title is not matched")'''