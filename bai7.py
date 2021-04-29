from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get(" http://practice.automationtesting.in/")




time.sleep(2)

account=driver.find_element_by_css_selector("#menu-item-50 > a")
account.click()
time.sleep(2)

input_m=driver.find_element_by_id("reg_email")
input_m.send_keys("abc@gmail.com")

time.sleep(2)

input_pass=driver.find_element_by_id("reg_password")
input_pass.send_keys("123456")

time.sleep(2)

click=driver.find_element_by_name("register")
click.click()

time.sleep(2)


driver.close()