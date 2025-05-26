from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_books_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://books.toscrape.com/")

    try:
        # Click on the "Science" category from the sidebar
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Science"))
        ).click()

        # Wait for the page to load and grab the first book's title
        book_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod h3 a"))
        ).get_attribute("title")

        print("✅ Test Passed: First Science Book Title =>", book_title)
    except Exception as e:
        print("❌ Test Failed:", e)
    finally:
        driver.quit()
