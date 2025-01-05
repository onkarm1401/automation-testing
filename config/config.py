import os

class Config:
    BASE_URL = "https://example.com"
    BROWSER = "chrome"
    TIMEOUT = 10
    HEADLESS = False
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
