from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from actions.headeractions import HeaderActions


class PageHeader(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = HeaderActions()

    # make search
    # view input
    # show suggester

    SEARCH_TXT = (By.ID, "SearchText")
    SEARCH_BTN = (By.ID, "search-btn")
    SEARCH_IMG = (By.XPATH, "//*[@id='search-btn']/img")
    SEARCH_SUGGESTER = (By.ID, "suggester-menu")

    def enter_search_phrase(self, search_phrase):
        print(f'Enter search phrase: {search_phrase}')
        search_textbox = self.driver.find_element(*self.SEARCH_TXT)
        search_textbox.clear()
        search_textbox.send_keys(search_phrase)

    def click_search_button(self):
        print('Click search button')
        self.click(self.SEARCH_BTN)

    def send_enter_to_search_form(self) -> None:
        self.driver.find_element(*self.SEARCH_TXT).send_keys(Keys.RETURN)

    def wait_for_suggester(self, search_phrase):
        self.enter_search_phrase(search_phrase)
        self.wait_for_clickable(self.SEARCH_SUGGESTER)
