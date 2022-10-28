import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
select_month="February"
select_year=2024
select_date="27"
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.find_element(by=By.XPATH,value="//input[@id='datepicker2']").click()
time.sleep(3)
select_monthoptions=driver.find_element(by=By.XPATH,value="//select[@class='datepick-month-year'][1]")
select_monthdropdown=Select(select_monthoptions)
select_monthvalues=select_monthdropdown.options
select_monthdropdown.select_by_value("2/2022")
select_yearoptions=driver.find_element(by=By.XPATH,value="//select[@class='datepick-month-year'][2]")
select_yeardropdown=Select(select_yearoptions)
select_yearvalues=select_yeardropdown.options
select_yeardropdown.select_by_visible_text("2024")
time.sleep(3)
driver.find_element(by=By.XPATH,value="//a[@title='Select Tuesday, Feb 27, 2024']").click()
time.sleep(3)
driver.close()