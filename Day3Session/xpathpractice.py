'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element(by=By.XPATH,value="//input[@id='twotabsearchtextbox']").send_keys("Laptops")
driver.find_element(by=By.XPATH,value="//input[@id='nav-search-submit-button']").click()
time.sleep(20)
driver.close()'''
#Xpath functions
#Text() function
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element(by=By.XPATH,value="//input[@id='twotabsearchtextbox']").send_keys("Laptops")
driver.find_element(by=By.XPATH,value="//input[@id='nav-search-submit-button']").click()
driver.find_element(by=By.XPATH,value="//a[text()=' Electronics ']").click()
time.sleep(20)
driver.close()'''

#OR function
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(by=By.XPATH,value="//input[@class='inputtext _55r1 _6luy' or input[@id='email']]").send_keys("nagiri@gmail.com")
time.sleep(10)

driver.close()'''

#And function

'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(by=By.XPATH,value="//input[@class='inputtext _55r1 _6luy' or input[@id='email']]").send_keys("nagiri@gmail.com")
driver.find_element(by=By.XPATH,value="//input[@name='pass' and @id='pass']").send_keys("tharun444")
time.sleep(10)

driver.close()'''

#contains and starts with function
#-----------------------------------
'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
#driver.find_element(by=By.XPATH,value="//a[contains(.,'Forgot')]").click()
driver.find_element(by=By.XPATH,value="//a[starts-with(text(),'Create New Account')]").click()
time.sleep(10)
driver.find_element(by=By.LINK_TEXT,value="Infosys").click()
driver.close()'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://money.rediff.com/")

driver.find_element(by=By.LINK_TEXT,value="Infosys").click()
time.sleep(10)
driver.close()

