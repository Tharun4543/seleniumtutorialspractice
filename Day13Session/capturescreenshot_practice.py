'''
    Hands on with capture screenshot using three built in methods
        1.save_screenshot
        2.get_screenshot_as_file
        3.get_screenshot_as_png(it will save the file in binary format)
        4.get_screenshot_as_base64(it will save the file in binary format)
'''
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
location=os.getcwd()
driver.get("https://omayo.blogspot.com/")
#driver.save_screenshot(location +"\\blogsave_screenshotmethod.png")
#driver.get_screenshot_as_file(location+"\\bloget_screenshotmethod.png")
#driver.get_screenshot_as_png()(it will save the file in binary format)
#driver.get_screenshot_as_base64()(it will save the file in binary format)
driver.close()