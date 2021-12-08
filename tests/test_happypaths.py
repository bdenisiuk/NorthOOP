import pytest

from pages.articlepage import ArticlePage
from pages.homepage import HomePage
from resources.data import *
from pages.cartpage import CartPage
from pages.grouppage import GroupPage


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


@pytest.mark.parametrize("url", ["https://north.pl"])
class TestHappyPaths(BaseTest):

    def test_grupy(self, url):
        self.homepage = HomePage(self.driver)
        self.homepage.open(url)
        self.homepage.header.actions.check_search_result(url)
        grouppage = GroupPage(self.driver)
        # grouppage.open('https://north.pl/ramki-wsadu,g675317.html')
        grouppage.open('https://north.pl/worki-prozniowe,g2056308.html')
        #grouppage.change_number_of_displayed_items('45')
        grouppage.displayed_items()
        #grouppage.check_delivery_time_clickable()

    @pytest.mark.skip
    def test_customer_buy_item_from_search_pay_online_with_paczkomaty_no_login(self, url):
        self.homepage = HomePage(self.driver)
        self.homepage.open(url)
        self.homepage.search(SEARCHED_ITEM)
        self.articlepage = ArticlePage(self.driver)
        self.articlepage.add_to_basket_and_proceed()
        self.cartpage = CartPage(self.driver)
        # cartPage.my_cart()
        # cart.go_to_delivery()
        # cart.choose_delivery()
        # cart.choose_payment()
        # cart.go_to_
        # cart.choose_login()
        # cart.go_to_customer_data
        # cart.fill_customer_data()

    @pytest.mark.skip
    def test_suggester(self, url):
        self.homePage = HomePage(self.driver)
        self.homePage.open(url)
        self.homePage.wait_for_suggester(SEARCHED_ITEM)

    @pytest.mark.skip
    def test_customer_buy_item_from_search_by_enter_pay_online_with_paczkomaty_no_login(self, url):
        self.homePage = HomePage(self.driver)
        self.homePage.open(url)
        self.homePage.search(SEARCHED_ITEM)

    @pytest.mark.skip
    def test_main_functions_are_working(self, url):
        self.homePage = HomePage(self.driver)
        self.homePage.open(url)
        self.homePage.main_functions_are_working()

# otwieramy strone
# wpisujemy nazwe produktu w szukajke
# -wyszukiwarka
# -- czyszczenie pola
# -- wyszukiwania przy uzyciu entera
# -- wyszukiwanie przy zuyciu myszki
# -- wyswietlanie sie podpowiedzi
# -- przewijanie podpowiedzi
# -- sprawdzanie czy podpowiedzi maja linki
#
#
# a)wybieramy lokowke z wynikow
# dodajemy do koszyka
#
# koszyk_1_twoj_koszyk
# koszyka_2_dostawa_i_platnosci
# koszyk_3_no_login
# koszyk_3b_dane
# koszyk_4_podsumowanie
