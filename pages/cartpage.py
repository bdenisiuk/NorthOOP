from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    CART_GO_TO_DELIVERY = (By.XPATH, "//div[contains(@class,'order')]//a[contains(@class,'btn')]")

    