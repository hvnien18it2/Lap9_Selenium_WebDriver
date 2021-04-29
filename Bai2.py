from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get(" http://practice.automationtesting.in/")


time.sleep(2)

driver.maximize_window()
time.sleep(2)
driver.close()