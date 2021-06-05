from Pages.BasePage import BasePage
from Pages.PageHeader import PageHeader
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
import time
# TODO: opisy bledow

class HomePageLocators:
    # textbox = _tb
    # button = _btn
    search_txt = (By.ID, "SearchText")
    search_btn = (By.ID, "search-btn")
    search_img = (By.XPATH, "//*[@id='search-btn']/img")
    search_suggester = (By.ID, "suggester-menu")


class HomePage(BasePage, PageHeader):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)
        self.open('https://north.pl')

    # def __enter_search_phrase(self, search_phrase):
    #     self.driver.find_element(*HomePageLocators.search_txt).clear()
    #     self.enter_text(HomePageLocators.search_txt, search_phrase)

        # search_textbox = self.driver.find_element(*HomePageLocators.search_txt)
        # search_textbox.clear()
        # search_textbox.send_keys(search_phrase)
        # return self
    #
    # def __click_search_button(self):
    #     self.click(HomePageLocators.search_btn)
    #     return self
    #
    #
    # def __enter_search_button(self):
    #     search_textbox = self.driver.find_element(*HomePageLocators.search_txt)
    #     search_textbox.send_keys(Keys.RETURN)
    #     return self

    def search(self, search_phrase):
        # self.__enter_search_phrase(self, search_phrase)
        # self.__click_search_button(self)
        PageHeader.search(self, search_phrase)
        return self


    def search_by_enter(self, search_phrase):
        self.__enter_search_phrase(search_phrase)
        self.__enter_search_button()

    def main_functions_are_working(self):
        search_textbox = self.driver.find_element(*HomePageLocators.search_txt)
        search_textbox.is_displayed()
        search_icon = self.driver.find_element(*HomePageLocators.search_img)
        search_icon.is_displayed()




    # wyszukiwarka
    # wizard
    # kafelki glowne
    # wyswietlanie grafik glownych
    # karuzela_artykulow
    # karuzela_marek
    # menu
    #
    #
    # search.is_visible()
    # search.display_inserted_text
    # search.activated_by_click
    # search.activated_by_enter
    # search.move_to_other_site
    # search.display_suggester

    # def search(self, search_term):
    #     self.driver.find_element(*HomePageLocators.search_txt).clear()
    #     self.enter_text(HomePageLocators.search_txt, search_term)
    #     self.click(HomePageLocators.search_submit_btn)

