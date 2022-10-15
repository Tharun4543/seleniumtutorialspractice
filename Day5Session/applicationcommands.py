#hands on applications commands
'''get() method
title(it is not a method,it is a keyword)
current_url(it is not a method,it is a keyword)
page_resource(it returns page resource)
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
url_title=driver.title
currenturl=driver.current_url
soucecode=driver.page_source
print(currenturl)
print(url_title)
print(soucecode)
driver.close()