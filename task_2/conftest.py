import pytest
from selenium import webdriver

@pytest.yield_fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

