import time
import driver as driver
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")
time.sleep(5)
driver.execute_script("window.scrollBy(0,800)"," ")

textbox_1=driver.find_element(by=By.XPATH,value="//textarea[@id='ta1']")
textbox_1.send_keys("Tharun is a waste fellow")
actions=ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").perform()
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys("c").perform()
time.sleep(3)
actions.send_keys(Keys.TAB).perform()
time.sleep(5)
textbox_2=driver.find_element(by=By.XPATH,value="//textarea[normalize-space()='The cat was playing in the garden.']")
textbox_2.clear()
time.sleep(3)
actions.key_down(Keys.CONTROL).send_keys("v").perform()
time.sleep(5)

driver.close()


