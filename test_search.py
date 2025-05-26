from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_amazon_search():
    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Go to Amazon India
        driver.get("https://www.amazon.in")

        # Wait for search bar
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("headphones")

        # Click search button
        search_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
        )
        search_button.click()

        # Wait for results by checking for the main product grid
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
        )

        # Assert something is returned in the page title
        assert "headphones" in driver.title.lower()

    finally:
        driver.quit()
