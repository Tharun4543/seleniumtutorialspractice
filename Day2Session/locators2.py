#CLASSNAME
#TAGNAME
#CSSSELECTOR[tag and ID,tag and class,tag and attribute,tag,class and attribute]

#CLASSNAME
'''from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
list1=driver.find_elements(by=By.CLASS_NAME,value="homeslider-container")
print(len(list1))
driver.close()
#Example2
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
list1=driver.find_elements(by=By.CLASS_NAME,value="quick-view")
print(len(list1))
driver.close()

#TagName
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
list1=driver.find_elements(by=By.TAG_NAME,value="a")
print(len(list1))
driver.close()'''



