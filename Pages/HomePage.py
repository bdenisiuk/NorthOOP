from Pages.BasePage import BasePage
from Pages.PageHeader import PageHeader
from selenium.webdriver.common.by import By


class HomePageLocators:
    # textbox = _tb
    # button = _btn
    search_tb = (By.ID, "SearchText")
    search_submit_btn = (By.XPATH, "//input[@id='SearchText']/../button")


class HomePage(BasePage):


    def main_functions_are_working(self):
        pass
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

    def search(self, search_term):
        self.driver.find_element(*HomePageLocators.search_tb).clear()
        self.enter_text(HomePageLocators.search_tb, search_term)
        self.click(HomePageLocators.search_submit_btn)
