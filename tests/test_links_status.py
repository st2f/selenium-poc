# tests/test_links_clickable.py
import os
import requests
import pytest
from pages.home_page import HomePage
from dotenv import load_dotenv

load_dotenv()

def test_all_links_status(browser):
    site_url = os.getenv("SITE_URL")
    home = HomePage(browser)
    home.go_to(site_url)

    links = home.get_all_links()
    assert links, "No links found on homepage"

    for link in links:
        response = requests.head(link, allow_redirects=True)
        assert response.status_code == 200, f"Link failed: {link} returned {response.status_code}"
