# test_search.py

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

        # Wait for the search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("headphones")

        # Wait for and click the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
        )
        search_button.click()

        # Wait for the title to update
        WebDriverWait(driver, 10).until(EC.title_contains("headphones"))

        # Assertion
        assert "headphones" in driver.title.lower()

    except Exception as e:
        print(f"\nTest failed due to: {e}\n")
        raise

    finally:
        driver.quit()
