from pages.articlepage import ArticlePage
from pages.grouppage import GroupPage
from pages.searchpage import SearchPage
from pages.basepage import BasePage

class ArticleActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def add_to_basket(self):
        # click add to basket

        self.click(ArticlePage.ADD_TO_BASKET)
        # confirm

    def confirm_purchase(self):
        self.click(ArticlePage.CONFIRM_PURCHASE)