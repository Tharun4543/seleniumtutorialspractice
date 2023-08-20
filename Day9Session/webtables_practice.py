'''
Hands on with
    1.find the no.of rows and no.of columns in the table
    2.Read specific row and column data
    3.Read all the rows and columns data
    4.Read data based on the condition

'''
import time
#import driver as driver
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
#find the no.of rows and no.of columns in the table
no_of_rows=driver.find_elements(by=By.XPATH,value="//table[@id='table1']//tbody//tr")
no_of_columns=driver.find_elements(by=By.XPATH,value="//table[@id='table1']//thead//tr//th")
total_rowvalue=len(no_of_rows) #5
total_colvalue=len(no_of_columns) #3'''
#find the specific row and specific column in the table
'''fifthrow_name=driver.find_element(by=By.XPATH,value="//table[@id='table1']//tbody//tr[4]//td[1]").text
fifthrow_place=driver.find_element(by=By.XPATH,value="//table[@id='table1']//tbody//tr[4]//td[3]").text
print(fifthrow_name,end="                ")
print(fifthrow_place)'''
#Read all the rows and columns in the table
'''for row in range(1,total_rowvalue+1):
    for col in range(1,total_colvalue+1):
        tabledata_value=driver.find_element(by=By.XPATH,value="//table[@id='table1']//tr["+str(row)+"]//td["+str(col)+"]").text
        print(tabledata_value,end="    ")
    print()'''
#Read the data in the table based on the condition

for row in range(1,total_rowvalue+1):
    list_value=driver.find_element(by=By.XPATH,value="//table[@id='table1']//tr["+str(row)+"]//td[3]")
    if list_value.text=="Pune" or list_value.text=="Bangalore" or list_value.text=="Mumbai":
        record_value=driver.find_element(by=By.XPATH,value="//table[@id='table1']//tr["+str(row)+"]")
        print(record_value.text)










driver.close()