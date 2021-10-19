from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from loguru import logger

class PageHeader():


    def __init__(self, driver):
        self.driver = driver



    # make search
    # view input
    # show suggester

    SEARCH_TXT = (By.ID, "SearchText")
    SEARCH_BTN = (By.ID, "search-btn")
    SEARCH_IMG = (By.XPATH, "//*[@id='search-btn']/img")
    SEARCH_SUGGESTER = (By.ID, "suggester-menu")

    LOGIN_STATUS = (By.ID, 'login_status')
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login_status']//*[contains(@class,'btn')]")


    def __enter_search_phrase(self, search_phrase):
        print('entering search phrase')
        search_textbox = self.driver.find_element(*PageHeader.SEARCH_TXT)
        search_textbox.clear()
        search_textbox.send_keys(search_phrase)
        print('exiting search phrase')

    def __click_search_button(self):
        BasePage.click(self, self.SEARCH_BTN)
        print('click search button done')

    # @logger.catch
    def search(self, search_phrase):
        self.__enter_search_phrase(search_phrase)
        self.__click_search_button()
        self.__check_search_result(self.driver.current_url)
        return self

    def __check_search_result(self, url):
        print('check search result')
        print(url)
        if "/s/" in url:
            print('/s/ w url')
            pass
            # szukajka
        elif "/karta/" in url:
            return print('brawo to karta produktu')
            # karta produktu

        elif ",g" in url:
            print('g w url')
            pass
        # grupa

        # https://north.pl/karta/67010214-koncowka-izolujaca-do-lokowki,736-WG-3530.html
        # karta produktu
        # https://north.pl/czesci-agd/czesci-do-lokowek/czesci-do-lokowek-braun,g886891.html
        # grupa ",g"
        # https://north.pl/s/?txtSzukaj=NI&search_type=&search_id=&f_producent=&f_rodzaj=&f_klas=0
        # szukajka z wynikami dla frazy
        # https://north.pl/s/?txtSzukaj=chujemuje
        # nie znaleziony

    def __enter_search_button(self):
        search_textbox = self.driver.find_element(*PageHeader.SEARCH_TXT)
        search_textbox.click()
        search_textbox.send_keys(Keys.RETURN)

    def wait_for_suggester(self, search_phrase):
        self.__enter_search_phrase(search_phrase)
        BasePage.wait_for_clickable(self, self.SEARCH_SUGGESTER)


