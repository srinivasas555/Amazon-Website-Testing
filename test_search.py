from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def test_amazon_search():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = uc.Chrome(options=options)
    
    try:
        driver.get("https://www.amazon.in/")
        print(driver.page_source)  # 👈 Add this line

        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("headphones")

        search_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
        )
        search_button.click()

        WebDriverWait(driver, 15).until(
            EC.title_contains("headphones")
        )

        print("Test Passed: Page Title =>", driver.title)

    finally:
        driver.quit()
