from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators:
    # textbox = _tb
    # button = _btn
    search_tb = (By.ID, "SearchText")
    search_submit_btn = (By.XPATH, "//input[@id='SearchText']/../button")


class HomePage(BasePage):

    def open(self, site):
        self.driver.get(site)
        assert "North - Części AGD i RTV - Dom jest w Twoich rękach" in self.driver.title

    def search(self, search_term):
        self.driver.find_element(*HomePageLocators.search_tb).clear()
        self.enter_text(HomePageLocators.search_tb, search_term)
        self.click(HomePageLocators.search_submit_btn)





