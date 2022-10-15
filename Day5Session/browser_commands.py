#hands on close() and quit() commands
#close() will close only one tab, it will not kill the process
#quit() will close all tabs opened in the browser, it will kill the process.

#close() command
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
driver.find_element(by=By.LINK_TEXT,value="Forgotten account?").click()
time.sleep(10)
driver.close()'''

#quit() command
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
driver.find_element(by=By.LINK_TEXT,value="Forgotten account?").click()
time.sleep(10)
driver.quit()