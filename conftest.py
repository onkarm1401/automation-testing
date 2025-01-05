import pytest
from utils.browser import Browser

@pytest.fixture(scope="session")
def browser():
    browser = Browser("chrome")
    yield browser
    browser.driver.quit()
