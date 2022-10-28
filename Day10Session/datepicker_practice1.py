import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://material.angular.io/components/datepicker/overview")
time.sleep(5)
driver.find_element(by=By.XPATH,value="//mat-datepicker-toggle[@class='mat-datepicker-toggle ng-tns-c150-3']//span[@class='mat-button-wrapper']//*[name()='svg']").click()







time.sleep(5)

driver.close()