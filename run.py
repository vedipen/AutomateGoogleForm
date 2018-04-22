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

print("\nAwards :")
awards = ["Mr. India award (Low attendance)","Lifetime achievement award (Student of the year)",
    "Ranchoddas Shamaldas award (Nerd)","Salman Bhai Award (Gets out of trouble easily)",
    "Munnabhai & circuit award (Best Friends)","Jimmy Shergill (Friendzoned)"]

minimalAwards = ["Mr. India","Lifetime","Ranchoddas","Salman","Munnabhai","Jimmy"]

for i in range(0,len(awards)):
    print(str(i+1) + " " + awards[i])

award = int(input("\nWhich award do you want to give? (Ex. 1) : "))
while award < 1 or award > 6 :
    award = int(input("Which award do you want to give? (Ex. 1) : "))
award-=1

person = input("Enter the name of the person you want to give (Ex. Ayush Varma): ")
times = int(input("Enter the number of times you want to submit the form (Ex. 10) : "))
while times < 1 :
    times = int(input("Enter the number of times you want to submit the form (Ex. 10) : "))
print("Awarding "+ person + " with " + str(times) + " " + awards[award] + "\n")

driver = webdriver.Chrome()
driver.get("https://goo.gl/axxoza")

inputElement = driver.find_element_by_name("identifier")
inputElement.send_keys(email + Keys.RETURN)
driver.implicitly_wait(10)

inputElement = driver.find_element_by_name("password")
inputElement.send_keys(password + Keys.RETURN)
driver.implicitly_wait(10)
WebDriverWait(driver, 100).until(EC.title_contains("Farewell Awards!"));

try:
    while times:
        WebDriverWait(driver, 10).until(EC.title_contains("Farewell Awards!"));
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[contains(text(), '" + minimalAwards[award] + "')]").click()
        personName = driver.find_element_by_xpath("//input[@type='text']")
        personName.send_keys(person)
        # time.sleep(5)
        driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[contains(text(), 'Your response has been recorded')]")
        times-=1
        print("Your response has been recorded. Remaining : " + str(times))
        driver.get("https://goo.gl/axxoza")

finally:
    driver.quit()
