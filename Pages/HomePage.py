from Pages.BasePage import BasePage
from Pages.PageHeader import PageHeader
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
# TODO: opisy bledow

class HomePage(BasePage):


    def __init__(self, driver: WebDriver):
        # super().__init__(driver)
        self.driver = driver
        self.header = PageHeader(self.driver)
        self.open('https://north.pl')

    def search(self, search_phrase):
        # self.header.search(search_phrase)
        self.header.Search.search(self, search_phrase)

    def wait_for_suggester(self, search_phrase):
        self.header.wait_for_suggester(search_phrase)

    def main_functions_are_working(self):
        search_textbox = self.driver.find_element(*HomePage.SEARCH_TXT)
        search_textbox.is_displayed()
        search_icon = self.driver.find_element(*HomePage.SEARCH_IMG)
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
    #     self.driver.find_element(*HomePageLocators.SEARCH_TXT).clear()
    #     self.enter_text(HomePageLocators.SEARCH_TXT, search_term)
    #     self.click(HomePageLocators.search_submit_btn)

