import pytest
from selenium import webdriver

@pytest.yield_fixture(scope='session')
def browser():
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    yield browser
    browser.quit()