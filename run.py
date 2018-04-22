from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

import time
import getpass

email = input("Enter your Somaiya ID : ")
email += "@somaiya.edu"
print("Email : "+email)
password = getpass.getpass('Password : ')

awards = ["Mr. India award (Low attendance)","Lifetime achievement award ( Student of the year)",
    "Ranchoddas Shamaldas award (Nerd)","Salman Bhai Award (Gets out of trouble easily)",
    "Munnabhai & circuit award (Best Friends)","Jimmy Shergill (Friendzoned)"]

minimalAwards = ["Mr. India","Lifetime","Ranchoddas","Salman","Munnabhai","Jimmy"]

for i in range(0,len(awards)):
    print(str(i+1) + " " + awards[i])

award = int(input("Which award do you want to give? (Ex. 1) : "))
while award < 1 or award > 6 :
    award = int(input("Which award do you want to give? (Ex. 1) : "))
award-=1

person = input("Enter the name of the person you want to give (Ex. Ayush Varma): ")

print("Awarding "+ person + " with "+ awards[award])

driver = webdriver.Chrome()
driver.get("https://goo.gl/axxoza")

inputElement = driver.find_element_by_name("identifier")
inputElement.send_keys(email + Keys.RETURN)
driver.implicitly_wait(10)

inputElement = driver.find_element_by_name("password")
inputElement.send_keys(password + Keys.RETURN)
driver.implicitly_wait(10)

try:
    WebDriverWait(driver, 100).until(EC.title_contains("Farewell Awards!"));
    driver.find_element_by_xpath("//*[contains(text(), '" + minimalAwards[award] + "')]").click()
    personName = driver.find_element_by_xpath("//input[@type='text']")
    personName.send_keys(person)
    # time.sleep(5)
    driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
    # time.sleep(5)

finally:
    driver.quit()
