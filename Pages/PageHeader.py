from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PageHeader():


    def __init__(self, driver):
        self.driver = driver

    WIZARD_DEVICE_TYPE = (By.ID, "wizzart-device-list")
    WIZARD_MANUFACTURER = (By.ID, "wizzart-brand-list")
    WIZARD_MODEL_NUMBER = (By.ID, "search_model")
    WIZARD_SEARCH_BUTTON = (By.ID, "search_btn")

    class Search():

        SEARCH_TXT = (By.ID, "SearchText")
        SEARCH_BTN = (By.ID, "search-btn")
        SEARCH_IMG = (By.XPATH, "//*[@id='search-btn']/img")
        SEARCH_SUGGESTER = (By.ID, "suggester-menu")

        def __init__(self, search_phrase):
            self.search_phrase = search_phrase

        def __enter_search_phrase(self, search_phrase):
            print('entering search phrase')
            search_textbox = self.driver.find_element(*PageHeader.SEARCH_TXT)
            search_textbox.clear()
            search_textbox.send_keys(search_phrase)

        def __click_search_button(self):
            BasePage.click(self, self.SEARCH_BTN)

        def search(self, search_phrase):
            self.__enter_search_phrase(search_phrase)
            self.__click_search_button()
            time.sleep(5)

        def __enter_search_button(self):
            search_textbox = self.driver.find_element(*PageHeader.SEARCH_TXT)
            search_textbox.click()
            search_textbox.send_keys(Keys.RETURN)

        def wait_for_suggester(self, search_phrase):
            self.__enter_search_phrase(search_phrase)
            BasePage.wait_for_clickable(self, self.SEARCH_SUGGESTER)


