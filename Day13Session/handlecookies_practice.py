'''
    Hands on with
        1.How to get a cookies.
        2.How to create a cookies.
        3.How to delete a cookies.
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
driver.get("https://www.globalsqa.com/demo-site/sliders/#Range")
#get cookies from webapplication
'''cookies_list=driver.get_cookies()
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie)
    #print(cookie.get('domain'),":",cookie.get('expiry'))'''
#create cookies from webapplication'''
'''cookies_list=driver.get_cookies()
print(len(cookies_list))
driver.add_cookie({'name':'Tharun','value':'cntharun'})
cookies_list=driver.get_cookies()
print(len(cookies_list))'''
#Delete a desire cookie from webapplication
'''cookies_list=driver.get_cookies()
print(len(cookies_list))
driver.delete_cookie('_gat_gtag_UA_67337609_1')
cookies_list=driver.get_cookies()
print(len(cookies_list))'''
#Delete all cookies from webapplication
cookies_list=driver.get_cookies()
print(len(cookies_list))
driver.delete_all_cookies()
cookies_list=driver.get_cookies()
print(len(cookies_list))
driver.close()