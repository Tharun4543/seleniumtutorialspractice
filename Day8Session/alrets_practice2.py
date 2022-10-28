#Hands on with alrets
#Example 1
#accepting the alret box with one button and printing the text in the console.
'''import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(by=By.XPATH,value="//button[text()='Click for JS Alert']").click()
alret_window=driver.switch_to.alert
time.sleep(3)
alret_window.accept()
time.sleep(5)
alret1_text=driver.find_element(by=By.XPATH,value="//p[@id='result']")
print(alret1_text.text)
driver.close()'''

#Example 2
#accepting the alret box with two buttons(i.e Ok button and cancel button) and printing the text in the console.
'''import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(by=By.XPATH,value="//button[text()='Click for JS Confirm']").click()
alret_window=driver.switch_to.alert
time.sleep(3)'''
#accept the OK button scenerio and print the text in the console.
'''alret_window.accept()
time.sleep(5)
alret1_text=driver.find_element(by=By.XPATH,value="//p[@id='result']")
print(alret1_text.text)
driver.close()'''
#accept the cancel button scenerio and print the text in the console.
'''alret_window.dismiss()
time.sleep(5)
alret1_text=driver.find_element(by=By.XPATH,value="//p[@id='result']")
print(alret1_text.text)
driver.close()'''

#Example 3
#Handle the alrets which contains two buttons(OK and cancel button) contains a one input box.
import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# 1Scenerio.
'''1.switch to the alret.
   2.pass the text in input box field
   3.accept the OK buttton 
driver.find_element(by=By.XPATH,value="//button[text()='Click for JS Prompt']").click()
alret_box=driver.switch_to.alert
alret_box.send_keys("Tharun is a waste fellow")
time.sleep(3)
alret_box.accept()
alret1_text=driver.find_element(by=By.XPATH,value="//p[@id='result']")
print(alret1_text.text)
driver.close()
'''
# 2Scenerio
'''
  1.switch to the alret.
  2.pass the text in input box field
  3.Click on cancel button
'''
driver.find_element(by=By.XPATH,value="//button[text()='Click for JS Prompt']").click()
alret_box=driver.switch_to.alert
alret_box.send_keys("Tharun is a waste fellow")
time.sleep(3)
alret_box.dismiss()
alret1_text=driver.find_element(by=By.XPATH,value="//p[@id='result']")
print(alret1_text.text)
driver.close()