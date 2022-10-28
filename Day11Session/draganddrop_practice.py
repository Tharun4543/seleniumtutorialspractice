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
driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager")
switch_frameele=driver.find_element(by=By.XPATH,value="(//iframe[@class='demo-frame lazyloaded'])[1]")
driver.switch_to.frame(switch_frameele)
source_image1=driver.find_element(by=By.XPATH,value="//img[@alt='The peaks of High Tatras']")
destination_img1=driver.find_element(by=By.XPATH,value="//div[@id='trash']")
source_image2=driver.find_element(by=By.XPATH,value="//img[@alt='Planning the ascent']")
destination_img2=driver.find_element(by=By.XPATH,value="//div[@id='trash']")
source_image3=driver.find_element(by=By.XPATH,value="//img[@alt='The chalet at the Green mountain lake']")
destination_img3=driver.find_element(by=By.XPATH,value="//div[@id='trash']")
source_image4=driver.find_element(by=By.XPATH,value="//img[@alt='On top of Kozi kopka']")
destination_img4=driver.find_element(by=By.XPATH,value="//div[@id='trash']")

actions=ActionChains(driver)
actions.drag_and_drop(source_image1,destination_img1).perform()
actions.drag_and_drop(source_image2,destination_img2).perform()
actions.drag_and_drop(source_image3,destination_img3).perform()
actions.drag_and_drop(source_image4,destination_img4).perform()
time.sleep(3)
driver.close()