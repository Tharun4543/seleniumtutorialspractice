#Hands on findelement and findelements() method
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
#locator matching with single element
'''driver.find_element(by=By.XPATH,value="//input[@id='inputValEnter']").send_keys("shirts")
time.sleep(10)
driver.close()
#locator matching with multiple web elements
links=driver.find_element(by=By.XPATH,value="")
print(links.text)
time.sleep(10)
driver.close()
#find element using incorrect locator
links=driver.find_element(by=By.XPATH,value="//div[@class='row lowerContent-foo']")
print(links.text)
time.sleep(10)
driver.close()'''



#find_elements method()
#locator matching with single element
'''links=driver.find_elements(by=By.XPATH,value="//a[text()='Lehenga']")
print(len(links))
print(links[0].text)
time.sleep(10)
driver.close()

#locator matching with multiple elements
links=driver.find_elements(by=By.XPATH,value="//div[@class='row lowerContent-footer']//a")
print(len(links))
for link in links:
    print(link.text)
time.sleep(10)
driver.close()

#find element using incorrect locator
note:
------
1.find_elements does not return an exception if locator is not found.
2.it returns 0 as a output in the console.
links=driver.find_elements(by=By.XPATH,value="//div[@class='row lowerContent']//a")
print(len(links))
for link in links:
    print(link.text)
time.sleep(10)
driver.close()'''
