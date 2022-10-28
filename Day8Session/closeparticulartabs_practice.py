import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element(by=By.LINK_TEXT,value="Help").click()
time.sleep(3)
driver.find_element(by=By.LINK_TEXT,value="Privacy").click()
time.sleep(3)
driver.find_element(by=By.LINK_TEXT,value="Terms").click()
time.sleep(3)
no_of_windows=driver.window_handles
for windows in no_of_windows:
    driver.switch_to.window(windows)
    if driver.title=="Privacy Policy – Privacy & Terms – Google" or driver.title=="Google Terms of Service – Privacy & Terms – Google":
        driver.close()