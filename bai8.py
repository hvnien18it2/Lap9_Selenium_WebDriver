from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path="C:\Selenium\chromedriver.exe"
driver=webdriver.Chrome(driver_path)

driver.get("https://the-internet.herokuapp.com")




time.sleep(2)

authen=driver.find_element_by_css_selector("#content > ul > li:nth-child(21) > a")
authen.click()
time.sleep(2)

username=driver.find_element_by_id("username")
username.send_keys("tomsmith")

time.sleep(2)

input_pass=driver.find_element_by_id("password")
input_pass.send_keys("SuperSecretPassword!")

time.sleep(2)

click=driver.find_element_by_css_selector("#login > button > i")
click.click()

time.sleep(2)

print(driver.title)

time.sleep(2)

driver.close()