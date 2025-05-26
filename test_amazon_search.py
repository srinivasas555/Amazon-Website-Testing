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
        # Check if CAPTCHA is present
        if "Enter the characters you see below" in driver.page_source:
            print("❌ CAPTCHA detected. Test aborted.")
