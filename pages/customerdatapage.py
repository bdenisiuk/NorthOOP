from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class CustomerDataPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
