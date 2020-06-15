from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd

#Setting path for chrome driver
#currently hardcoded but can use os varibles

path=r'C:\Users\Huma\Desktop\chromedriver.exe'

chrome_options = Options()

#creating webdriver object
driver = webdriver.Chrome(path, options=chrome_options)

#getting drame website
driver.get('https://www.dramexchange.com/')

#counting no. of rows and columns to verify find_element_by_xpath is working correctly or not
no_of_rows=len(driver.find_elements_by_xpath('//*[@id="tb_NationalDramSpotPrice"]/tr'))
no_of_columns=len(driver.find_elements_by_xpath('//*[@id="tb_NationalDramSpotPrice"]/tr[1]/td'))

#getting element
element_to_be_scarped=driver.find_elements_by_xpath('//*[@id="tb_NationalDramSpotPrice"]/tr[3]/td[6]')

#got a list in element_to_be_scarped
for val in element_to_be_scarped:
    print(val.text)