from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_amazon_search():
    # Setup
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.amazon.in")

   try:
    # your Selenium test logic here
    print("❌ CAPTCHA detected. Test aborted.")
except Exception as e:
    print(f"An error occurred: {e}")
