import pytest
from selenium import webdriver

APP_URL = "https://google.com"

def test_open_url():
    driver = webdriver.chrome
    driver.get(APP_URL)