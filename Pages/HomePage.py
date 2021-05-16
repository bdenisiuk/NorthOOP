from Pages.BasePage import BasePage
import pytest

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def open(self, site):
        self.driver.get(site)
        assert "North - Części AGD i RTV - Dom jest w Twoich rękach" in self.driver.title





