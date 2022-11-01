'''
    Hands on with
        1.download a file in default location
        2.download a file in desired location
'''
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/p/page7.html")
driver.maximize_window()

#Download a file in default location

driver.find_element(by=By.LINK_TEXT,value="ZIP file").click()
time.sleep(3)
driver.close()'''

#Download a file in desired location
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\ntharun\\PycharmProjects\\seleniumtutorialspractice\\Day12Session"})
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://omayo.blogspot.com/p/page7.html")
driver.maximize_window()
#Download a file in Desired location
driver.find_element(by=By.LINK_TEXT,value="ZIP file").click()
time.sleep(3)
driver.close()'''

#Download a file in current folder location
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

chrome_options=webdriver.ChromeOptions()
location=os.getcwd()
chrome_options.add_experimental_option("prefs",{"download.default_directory":location})
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://omayo.blogspot.com/p/page7.html")
driver.maximize_window()

driver.find_element(by=By.LINK_TEXT,value="ZIP file").click()
time.sleep(3)
driver.close()'''