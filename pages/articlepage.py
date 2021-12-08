from pages.basepage import BasePage
from pages.cartpage import CartPage
from selenium.webdriver.common.by import By


class ArticlePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_basket_and_proceed(self):
        print(self.driver.current_url)
        self.click(self.ADD_TO_BASKET)
        self.click(self.CONFIRM_PURCHASE)
        # return CartPage(self.driver)
    # TODO Jak zwracac Page z funkcji tak jak tutaj zeby wrocil obiekt do test_happypaths ? czy olac zwracanie skoro od nowa wywloujem instancje strony


    def add_to_basket_and_get_back(self):
        self.click(self.ADD_TO_BASKET)
        self.click(self.ADD_TO_BASKET_GET_BACK)


    ADD_TO_BASKET = (By.XPATH, "//div[@class='mt-2']/*[contains(@class,'btn')]")
    CONFIRM_PURCHASE = (By.XPATH, "//div[@class='modal-dialog modal-lg']//a[contains(text(),'koszyk')]")
    ADD_TO_BASKET_GET_BACK = (By.XPATH, "//div[@id='article-choose-modal']//div[contains(@class,'modal-footer')]//a[contains(@class,'btn-secondary')]")
