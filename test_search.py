# test_search.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_amazon_search():
    # Launch Chrome browser
    driver = webdriver.Chrome()

    # Open Amazon India
    driver.get("https://www.amazon.in")

    # Maximize the window (optional but recommended)
    driver.maximize_window()

    # Wait for the search box to be available and input the text
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("headphones")

    # Wait for the search button and click it
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
    )
    search_button.click()

    # Wait until the page title contains the search term
    WebDriverWait(driver, 10).until(EC.title_contains("headphones"))

    # Assert that the search term is in the page title
    assert "headphones" in driver.title.lower()

    # Close the browser
    driver.quit()
