# Hands on with Alrets

# Example for accepting the alret with single ok button
'''import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(by=By.XPATH,value="//input[contains(@id,'alert1')]").click()
alret_window=driver.switch_to.alert
time.sleep(5)
alret_window.accept()
driver.close()'''

# Example 2
# Hands on with alrets which contains multiple buttons.
'''import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(by=By.XPATH,value="//input[contains(@id,'confirm')]").click()'''

# Accepting the alret button scenerio.
'''alret_window=driver.switch_to.alert
time.sleep(5)
alret_window.accept()
driver.close()'''

'''#Dismiss the alret button scenerio.
alret_window=driver.switch_to.alert
time.sleep(5)
alret_window.dismiss()
driver.close()'''

# Example 3
# Hands on with alrets which contains multiple buttons and text input box.
import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(by=By.XPATH, value="//input[contains(@id,'prompt')]").click()
alret_window = driver.switch_to.alert
alret_window.send_keys("Tharun is a waste fellow")
time.sleep(5)
alret_window.accept()
driver.close()
