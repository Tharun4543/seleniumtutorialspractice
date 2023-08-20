#CSSSELECTOR[tag and ID,tag and class,tag and attribute,tag,class and attribute]
import time

#Tag with ID
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
driver.find_element(by=By.CSS_SELECTOR,value="input#email").send_keys("abc.com")
driver.find_element(by=By.CSS_SELECTOR,value="input#passwd").send_keys("xyz")
driver.find_element(by=By.CSS_SELECTOR,value="button#SubmitLogin").click()
time.sleep(10)
driver.close()

#Tag with Name
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
driver.find_element(by=By.CSS_SELECTOR,value="input.is_required").send_keys("abc.com")
driver.find_element(by=By.CSS_SELECTOR,value="input.is_required").send_keys("xyz")

time.sleep(10)
driver.close()


#Tag with attribute
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login")
driver.find_element(by=By.CSS_SELECTOR,value="[type=submit]").click()
time.sleep(10)
driver.close()

#Tag with class and attribute
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login")
driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext[type=password]").send_keys("xyz")
time.sleep(10)
driver.close()



