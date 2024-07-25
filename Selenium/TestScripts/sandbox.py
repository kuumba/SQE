import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_select_dropdown(driver):
    # Navigate to the page with the dropdown
    driver.get("https://qavbox.github.io/demo/signup")

    # Locate the dropdown element by its id, name, or xpath
    dropdown_element = driver.find_element(By.ID, "dropdown_id")

    # Create a Select object
    select = Select(dropdown_element)

    # Select by visible text
    select.select_by_visible_text("Option Text")

    # Alternatively, you can select by value or by index
    # select.select_by_value("option_value")
    # select.select_by_index(1)

    # Assert that the correct option is selected
    selected_option = select.first_selected_option
    assert selected_option.text == "Option Text"

if __name__ == "__main__":
    pytest.main()
