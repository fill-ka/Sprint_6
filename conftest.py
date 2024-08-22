import pytest
from selenium import webdriver


@pytest.fixture
def start_and_stop_browser():
    start_and_stop_browser = webdriver.Firefox()
    yield start_and_stop_browser
    start_and_stop_browser.quit()