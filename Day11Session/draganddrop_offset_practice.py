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
driver.get("https://www.globalsqa.com/demo-site/sliders/#Range")
time.sleep(3)
switch_frameele=driver.find_element(by=By.XPATH,value="//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(switch_frameele)
time.sleep(3)
min_slider=driver.find_element(by=By.XPATH,value="//span[1]")
max_slider=driver.find_element(by=By.XPATH,value="//span[2]")
print("Before moving the slider values are")
print(min_slider.location)
print(max_slider.location)
actions=ActionChains(driver)
actions.drag_and_drop_by_offset(min_slider,79,0).perform()
actions.drag_and_drop_by_offset(max_slider,-64,0).perform()
time.sleep(3)
print("After moving the slider values are")
print(min_slider.location)
print(max_slider.location)
time.sleep(3)
driver.close()