from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import pytest
import time

def test_amazon_search():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.send_keys("watch")
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    assert "watch" in driver.title.lower()
    driver.quit()
