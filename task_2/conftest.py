import pytest
from selenium import webdriver
import os
from sys import platform

@pytest.yield_fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    if platform == "win32":
        os.system("taskkill /im chromedriver.exe")




