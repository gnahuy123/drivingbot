from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from playsound import playsound
from random import randint

browser = webdriver.Chrome()

username = '670F06112003'
password = '200306'

browser.get('https://booking.bbdc.sg/#/login?redirect=%2Fhome%2Findex')

idLogin = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'input-8')))
idLogin.send_keys(username)

# Wait for the password input field to be present
idPassword = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'input-15')))
idPassword.send_keys(password)

# Wait for the login button to be clickable
loginButton = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'v-btn')))
loginButton.click()

# Captcha page
captcha_input = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'input-30')))

# Prompt the user to input the CAPTCHA manually
captcha_text = input("Please enter the CAPTCHA text manually Press enter when done: ")

# Fill the CAPTCHA input field with the user-provided text
captcha_input.send_keys(captcha_text)

loginButton = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'v-btn__content')))
loginButton.click()

input("press enter to start refreshing")

xpath = "//div[@class='calendar-col col']"
 # Replace with the XPath of the element you want to monitor

initial_html =  (browser.find_element(By.XPATH, xpath)).get_attribute("outerHTML")

while True:
    try:
        browser.refresh()
        WebDriverWait(browser, 30).until_not(EC.visibility_of_element_located((By.XPATH, "//*[name()='circle' and contains(@class,'v-progress')]")))
        after_html =  (browser.find_element(By.XPATH, xpath)).get_attribute("outerHTML")
        if after_html == initial_html:
            time.sleep(randint(10,15))
        else:
            playsound(r"C:\Users\Tan\Documents\GitHub\drivingbot\drivingbot\alarm.mp3")
            print("slots are open!!!")
            input("press enter to start refreshing")
    except NoSuchElementException:
        print("Element not found.")
        break
    except Exception as e:
        print("An error occurred:", e)

# Close the browser
browser.quit()