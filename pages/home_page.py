# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to(self, url):
        self.browser.get(url)

    def get_all_links(self):
        # Wait for post links to be visible
        wait = WebDriverWait(self.browser, 10)
        posts = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".post-card .post-title a"))
        )
        return [p.get_attribute("href") for p in posts if p.get_attribute("href")]
