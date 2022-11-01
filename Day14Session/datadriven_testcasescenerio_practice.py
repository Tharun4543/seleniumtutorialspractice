'''
    Hands on with Datadriven testcases

'''
from selenium.webdriver.support.select import Select
import XLutils_functions_file as utils
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--disable-notifications")
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(options=chromeoptions)
driver.maximize_window()
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
filename = "C:\\PERSONALFOLDERS\\SELENIUMDEC\\Datadriventestcases.xlsx"

max_rowvalue = utils.getRowCount(filename, "Sheet1")
for row in range(2, max_rowvalue + 1):
    pamount = utils.readData(filename, "Sheet1", row, 1)
    ROI = utils.readData(filename, "Sheet1", row, 2)
    period1 = utils.readData(filename, "Sheet1", row, 3)
    period2 = utils.readData(filename, "Sheet1", row, 4)
    frequency = utils.readData(filename, "Sheet1", row, 5)
    maturity_value = utils.readData(filename, "Sheet1", row, 6)
    driver.find_element(by=By.XPATH, value="//input[@id='principal']").send_keys(pamount)
    driver.find_element(by=By.XPATH, value="//input[@id='interest']").send_keys(ROI)
    driver.find_element(by=By.XPATH, value="//input[@id='tenure']").send_keys(period1)
    period_drpdown = Select(driver.find_element(by=By.XPATH, value="//select[@id='tenurePeriod']"))
    period_drpdown.select_by_visible_text(period2)
    frequency_dropdown = Select(driver.find_element(by=By.XPATH, value="//select[@id='frequency']"))
    frequency_dropdown.select_by_visible_text(frequency)
    driver.find_element(by=By.XPATH, value="//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    actual_value = driver.find_element(by=By.XPATH, value="//span[@id='resp_matval']//strong").text
    if float(maturity_value) == float(actual_value):
        print("Testcase passed")
        utils.writeData(filename, "Sheet1", row, 8, 'Pass')
        utils.fillGreenColor(filename, "Sheet1", row, 8)
    else:
        print("Testcase failed")
        utils.writeData(filename, "Sheet1", row, 8, 'Fail')
        utils.fillRedColor(filename, "Sheet1", row, 8)
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//img[@class='PL5']").click()
time.sleep(2)
driver.close()

'''
            Good job Tharun:)
            keep it up!!!
'''
