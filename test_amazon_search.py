import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_amazon_search():
    # Setup: Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Step 1: Open Amazon
        driver.get("https://www.amazon.in")

        # Step 2: Find the search box and enter "laptop"
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        time.sleep(3)
        
        # Step 3: Verify results are displayed
        results = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
        assert len(results) > 0, "❌ No results found!"

        print("✅ Amazon search test passed!")

    except Exception as e:
        print(f"❌ CAPTCHA detected or other error: {e}")
        assert False  # Fail the test on any exception
    
    finally:
        # Cleanup
        driver.quit()
