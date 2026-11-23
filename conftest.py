import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()

    # options.add_argument("--headless=new")

    chrome = webdriver.Chrome(options=options)
    chrome.maximize_window()
    chrome.implicitly_wait(2)

    request.node.driver = chrome

    yield chrome

    chrome.quit()