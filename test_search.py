import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_amazon_search():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--user-data-dir=C:/Users/srini/AppData/Local/Google/Chrome/User Data")  # 👈 Use your profile
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://www.amazon.in/")
        
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        ).send_keys("headphones")

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
        ).click()

        WebDriverWait(driver, 15).until(
            EC.title_contains("headphones")
        )

        print("✅ Test Passed: Page Title =>", driver.title)
    finally:
        input("Press Enter to close...")
        driver.quit()
