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
number_of_windows=driver.window_handles
print(len(number_of_windows))
for windows in number_of_windows:
    driver.switch_to.window(windows)
    #print(driver.title)
    if driver.title=="Google Account Help":
        driver.switch_to.window(windows)
        describe_value=driver.find_element(by=By.XPATH,value="//input[@class='promoted-search__input']")
        describe_value.send_keys("Tharun is a wastefellow")
        time.sleep(2)
        driver.find_element(by=By.LINK_TEXT,value="Control what others see about you across Google services").click()
        if driver.title=="Control what others see about you across Google services - Computer - Google Account Help":
            print("you have done good job dear!!")
        else:
            print("Please practice more dear!!")
        break


time.sleep(5)
driver.quit()