from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pytest

import calendar
import time
from datetime import datetime


driver = webdriver.Chrome()

def test_page_load():
    driver.get("https://qavbox.github.io/demo/signup")
    assert driver.title == "Registration Form"

def test_positive_form_submission():
    driver.find_element(By.ID, "username").send_keys("JohnDoe")
    driver.find_element(By.ID, "email").send_keys("JohnDoe@gmail.com")
    driver.find_element(By.ID, "tel").send_keys("954-903-7336")

    dropdown_element = driver.find_element(By.NAME, "sgender")    
    select = Select(dropdown_element)
    select.select_by_visible_text("Male")
    selected_option = select.first_selected_option

    radio_button = driver.find_element(By.XPATH, "//input[@value='three']")
    radio_button.click()

    checkbox = driver.find_element(By.ID, "ip")
    checkbox.click()

    multiselect_dropdown_element = driver.find_element(By.ID, "tools")    
    select = Select(multiselect_dropdown_element)
    select.select_by_visible_text("Selenium")
    multi_selected_option = select.first_selected_option

    assert selected_option.text == "Male"
    assert radio_button.is_selected
    assert checkbox.is_enabled
    assert multi_selected_option.is_enabled


    driver.find_element(By.ID, "submit").submit
#   driver.find_element(By.ID, "fax").send_keys("954-123-4567")

def test_screenshots():
    now = datetime.now()
    formatted_datetime = now.strftime("%m%d%Y.%H%M%S")
    driver.save_screenshot('./screenshots/' + formatted_datetime + ".png")
    print(formatted_datetime)

    driver.quit()
