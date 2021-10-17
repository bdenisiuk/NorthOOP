from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ArticlePage(BasePage):

    def add_to_basket(self):
        #click add to basket
        btn = "//div[@class='mt-2']/*[contains(@class,'btn')]"
        self.click(By.XPATH, btn)
        #confirm
        potwierdz_koszyk = "//div[@class='modal-dialog modal-lg']//a[contains(text(),'koszyk')]"
        self.click(By.XPATH, potwierdz_koszyk)