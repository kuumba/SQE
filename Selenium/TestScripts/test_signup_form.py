from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

import calendar
import time
from datetime import datetime


driver = webdriver.Chrome()

def test_page_load():
    driver.get("https://qavbox.github.io/demo/signup")
    assert driver.title == "Registration Form"

def test_form_submission():
    driver.find_element(By.ID, "username").send_keys("JohnDoe")
    driver.find_element(By.ID, "email").send_keys("JohnDoe@gmail.com")
    driver.find_element(By.ID, "tel").send_keys("954-903-7336")
    driver.find_element(By.ID, "submit").submit
#   driver.find_element(By.ID, "fax").send_keys("954-123-4567")

def test_screenshots():
    now = datetime.now()
   # driver.save_screenshot(now + ".jpg")
    formatted_datetime = now.strftime("%m%d%Y.%H%M%S")
    driver.save_screenshot('./screenshots/' + formatted_datetime + ".png")
    print(formatted_datetime)

    driver.quit()
