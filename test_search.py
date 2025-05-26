import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_amazon_search():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://www.amazon.in/")

        # Wait for search box and type query
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("headphones")

        # Wait for and click search button
        search_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
        )
        search_button.click()

        # Wait for page title or result
        WebDriverWait(driver, 15).until(
            EC.title_contains("headphones")
        )

        print("Final Page Title:", driver.title)
        assert "headphones" in driver.title.lower()

    finally:
        driver.quit()
