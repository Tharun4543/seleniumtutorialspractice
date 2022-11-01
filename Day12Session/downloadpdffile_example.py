import time

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs",{"download.default_directory":"location","plugins.always_open_pdf_externally":True})
driver=webdriver.Chrome()
