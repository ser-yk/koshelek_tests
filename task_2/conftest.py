import pytest
from selenium import webdriver
import os

@pytest.yield_fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    os.system("taskkill /im chromedriver.exe")



