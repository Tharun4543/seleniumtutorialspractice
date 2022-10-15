#Hands on is_selectedcommand
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?next=https%3A%2F%2Fwww.facebook.com%2Fcampaign%2Flanding.php%3Fcampaign_id%3D14884913640%26extra_1%3Ds%257Cc%257C550525805424%257Cb%257Cfacebook%2Bcom%2B%2523%257C%26placement%26creative%3D550525805424%26keyword%3Dfacebook%2Bcom%2B%2523%26partner_id%3Dgooglesem%26extra_2%3Dcampaignid%253D14884913640%2526adgroupid%253D128696221352%2526matchtype%253Db%2526network%253Dg%2526source%253Dnotmobile%2526search_or_content%253Ds%2526device%253Dc%2526devicemodel%253D%2526adposition%253D%2526target%253D%2526targetid%253Dkwd-498889442776%2526loc_physical_ms%253D1007740%2526loc_interest_ms%253D%2526feeditemid%253D%2526param1%253D%2526param2%253D%26gclid%3DEAIaIQobChMIscv87Yzc-gIVmZhmAh0F6QVkEAAYASAAEgLbqvD_BwE&locale=en_GB&display=page")
driver.maximize_window()
status_frbutton=driver.find_element(by=By.XPATH,value="//label[normalize-space()='Female']")
#print(status_frbutton.is_selected())
status_frbutton.click()
time.sleep(10)
print(status_frbutton)
#print(driver.find_element(by=By.XPATH,value="//label[normalize-space()='Female']").is_selected())
time.sleep(10)
driver.close()