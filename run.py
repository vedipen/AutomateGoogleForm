from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

import getpass

email = input("Enter your Somaiya ID : ")
email += "@somaiya.edu"
print("Email : "+email)
password = getpass.getpass('Password : ')

driver = webdriver.Chrome()
driver.get("https://goo.gl/axxoza")

inputElement = driver.find_element_by_name("identifier")
inputElement.send_keys(email + Keys.RETURN)
driver.implicitly_wait(10)

inputElement = driver.find_element_by_name("password")
inputElement.send_keys(password + Keys.RETURN)
driver.implicitly_wait(10)
