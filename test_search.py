from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_amazon_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://www.amazon.in")

        # Wait for search box and send query
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("headphones")

        # Click the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
        )
        search_button.click()

        # Wait for search results to appear by checking for a results container
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-color-state"))
        )

        # Now safely check the page title
        assert "headphones" in driver.title.lower()

    finally:
        driver.quit()
