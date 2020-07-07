from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def switch_button_present(self):
        assert self.is_element_present(*MainPageLocators.LANGUAGE_CHANGE_BUTTON), 'Button is not present'

    def switch_language(self, part_url, language):
        button = self.browser.find_element(*MainPageLocators.LANGUAGE_CHANGE_BUTTON)
        button.click()

        how, what = MainPageLocators.TABLE_WITH_LANGUAGE
        what = what + f'[text()="{language}"]'
        print(what)
        language_link = self.browser.find_element(how, what)
        language_link.click()
        time.sleep(2)
        assert self.browser.current_url.endswith(part_url), \
            f'Invalid url: {self.browser.current_url}, except ends with {part_url}'



