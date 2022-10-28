import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
select_month="March 2024"
select_date="31"

driver.get("https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker")
time.sleep(5)
frame1=driver.find_element(by=By.XPATH,value="//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(frame1)
time.sleep(4)
driver.find_element(by=By.XPATH,value="//input[@id='datepicker']").click()
time.sleep(5)
while True:
    month_value=driver.find_element(by=By.XPATH,value="//div[@class='ui-datepicker-title']").text
    if month_value==select_month:
        break
    else:
        driver.find_element(by=By.XPATH,value="//span[text()='Next']").click()
date_values=driver.find_elements(by=By.XPATH,value="//table[@class='ui-datepicker-calendar']//tr//td")
for value in date_values:
    if value.text==select_date:
        value.click()
        break
time.sleep(5)
driver.close()