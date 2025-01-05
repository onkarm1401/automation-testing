from selenium import webdriver
from config.config import Config

class Browser:
    def __init__(self, browser_type):
        self.browser_type = browser_type
        self.driver = None

    def open(self, url):
        if self.browser_type == "chrome":
            self.driver = webdriver.Chrome()
        self.driver.get(url)

    def login(self, username, password):
        # Logic for login
        pass

    def is_logged_in(self):
        # Logic to verify if logged in
        return True
