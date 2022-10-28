#How to handle authentication popup windows
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://guest:guest@jigsaw.w3.org/HTTP/Basic/")
time.sleep(5)
driver.close()

