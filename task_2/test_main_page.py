import pytest
from pages.main_page import MainPage



@pytest.mark.parametrize('link', ["https://coinmarketcap.com"])
class TestSwitchLanguage:
    @pytest.mark.skip
    def test_change_language_button_is_present_on_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.switch_button_present()


    @pytest.mark.parametrize('part_url,language', [('/de/', 'Deutsch'), ('/', 'English'), ('/es/', 'Español'),
                                                   ('/fil/', 'Filipino'), ('/fr/', 'Français'),
                                                   ('/hi/', 'हिन्दी'), ('/it/', 'Italiano'), ('/ja/', '日本語'),
                                                   ('/ko/', '한국어'),
                                                   ('/pt-br/', 'Português Brasil'), ('/ru/', 'Русский'),
                                                   ('/tr/', 'Türkçe'),
                                                   ('/vi/', 'Tiếng Việt'), ('/zh/', '简体中文'), ('/zh-tw/', '繁體中文')
                                                   ])
    def test_url_after_switch_language(self, browser, link, language, part_url):
        page = MainPage(browser, link)
        page.open()
        page.switch_language(part_url, language)


    @pytest.mark.parametrize('lang, url', [('de', 'https://coinmarketcap.com/de/'),
                                           ('en', 'https://coinmarketcap.com/'),
                                           ('es', 'https://coinmarketcap.com/es/'),
                                           ('fil', 'https://coinmarketcap.com/fil/'),
                                           ('fr', 'https://coinmarketcap.com/fr/'),
                                           ('hi', 'https://coinmarketcap.com/hi/'),
                                           ('it', 'https://coinmarketcap.com/it/'),
                                           ('ja', 'https://coinmarketcap.com/ja/'),
                                           ('ko', 'https://coinmarketcap.com/ko/'),
                                           ('pt-br', 'https://coinmarketcap.com/pt-br/'),
                                           ('ru', 'https://coinmarketcap.com/ru/'),
                                           ('tr', 'https://coinmarketcap.com/tr/'),
                                           ('vi', 'https://coinmarketcap.com/zh,'),
                                           ('zh', 'https://coinmarketcap.com/zh/'),
                                           ('zh-tw', 'https://coinmarketcap.com/zh,tw')])
    def test_tag_html_attribute_language(self, browser, link, lang, url):
        page = MainPage(browser, url)
        page.open()
        actual_lang = page.get_language_from_html_tag()
        assert actual_lang == lang, f'Html attribute lang should be - "{lang}", but actual - "{actual_lang}" '
