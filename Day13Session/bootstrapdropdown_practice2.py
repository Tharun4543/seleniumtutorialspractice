#Hands on with bootstrap dropdown Example2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.execute_script("window.scrollBy(0,1200)"," ")
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(by=By.XPATH,value="//span[@id='select2-billing_country-container']").click()
country_list=driver.find_elements(by=By.XPATH,value="//span[@class='select2-results']//ul//li")
#print(len(country_list))
for country in country_list:
    if country.text=="Spain":
        country.click()
        break
time.sleep(3)
driver.close()