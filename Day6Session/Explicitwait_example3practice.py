from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")
search_string=driver.find_element(by=By.XPATH,value="//input[@title='Search']")
search_string.send_keys("selenium")
search_string.submit()
wait=WebDriverWait(driver,10)
searched_webpage=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[text()='Selenium']")))

driver.close()