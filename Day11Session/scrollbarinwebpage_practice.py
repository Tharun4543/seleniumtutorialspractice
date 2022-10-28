'''
   Hands on with scroll bar in browser
'''
import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)
#Scroll the bar based on the pixels
'''driver.execute_script("window.scrollBy(0,400)"," ")
value=driver.execute_script("return window.pageYOffset;")
time.sleep(5)
print(value)'''
#Scroll the bar until the element is visible
'''laptop_discount=driver.find_element(by=By.XPATH,value="//span[contains(text(),'Up to 50% off | Refurbished laptops, phones and mo')]")
driver.execute_script("arguments[0].scrollIntoView();",laptop_discount)
time.sleep(5)
driver.close()'''
#Scroll the bar until the webpage till end
'''driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.close()'''
#Scroll the bar until the webpage till end and again scroll to top
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)
driver.close()