from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_books_homepage():
    driver = webdriver.Chrome()
    driver.get("https://books.toscrape.com/")
    
    assert "Books to Scrape" in driver.title
    
    # Example: find and click first book
    first_book = driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a")
    first_book.click()
    
    assert "catalogue" in driver.current_url

    time.sleep(2)
    driver.quit()
