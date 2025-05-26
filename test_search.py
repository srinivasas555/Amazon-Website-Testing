# test_search.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_amazon_search():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")
    
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("headphones")
    
    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    
    assert "headphones" in driver.title.lower()
    driver.quit()
