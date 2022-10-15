'''1.child
2.parent
3.Ancestor
4.sibiling
5.following-sibiling
6.preceding_sibiling
7.descedent
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://money.rediff.com/companies")
driver.find_element(by=By.LINK_TEXT,value='Zomato').click()
time.sleep(10)
driver.close()