import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class PageHeader():

    search_txt = (By.ID, "SearchText")
    search_btn = (By.ID, "search-btn")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def __click_search_button(self):
        # self.click(self.search_btn)
        BasePage.click(self, self.search_btn)
        time.sleep(4)
        return self

    def __enter_search_phrase(self, search_phrase):
        print('entering search phrase')

        self.driver.find_element(*self.search_txt).clear()
        BasePage.enter_text(self, self.search_txt, search_phrase)
        time.sleep(4)
        # self.enter_text(self.search_txt, search_phrase)

    def search(self, search_phrase):
        self.__enter_search_phrase(search_phrase)
        self.__click_search_button()
        return self