from selenium.webdriver.common.by import By


class BasePageLocators:
    HTML_TAG = (By.TAG_NAME, 'html')


class MainPageLocators:
    LANGUAGE_CHANGE_BUTTON = (By.CSS_SELECTOR, "div.cmc-popover__trigger button")
    TABLE_WITH_LANGUAGE = (By.XPATH, '//div[@class="cmc-popover__dropdown"]//a')

