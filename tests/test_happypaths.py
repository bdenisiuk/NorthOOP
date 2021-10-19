# happy path
# klient wyszukuje lokowke, wrzuca do koszyka, wybiera platnosc online i wysylke paczkomatem, nie zaklada konta

# testy funkcjonalne
# strona glowna (sprawdzamy czy sie zaladowala poprawnie, czy sa widoczne glowne elementy,
# czy wyszukiwarka jest aktywna, czy koszyk pusty)


# happy paths
import time

import pytest
from Pages.HomePage import HomePage
from Pages.ArticlePage import ArticlePage
from Pages.PageHeader import PageHeader
from Pages.BasePage import BasePage


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

item = 'Lokówka'

class TestLogin(BaseTest):

    #polimorfizm powiniene dostosowac sie do wyswietlanej strony
    #praktycznie powinny sie zmienic tylko zmienne podajace miejsce loginu, hasla i przejscia dalej czy tez wyniki logowania (poprawny, niepoprawny)

    #co trzeba zrobic :
    #przecwiczyc polimorfizm

    ## polimorfizm - uzycie metody o tej samej nazwie w roznych klasach
    klasa logowanie
    metody logowanie poprawne
    i logowanie niepoprawne

class LoginFromMainPage(BasePage):

    BasePage.click(PageHeader.LOGIN_STATUS)
    BasePage.click(PageHeader.LOGIN_BUTTON)


    pass

class LoginFromBasket():

    pass

    klasa logowanie z poziomu strony glownej
    wybranie miejsca do wpisania loginu
    wybranie miejsca do wpisania hasla
    wybranie przycisku do zatwierdzenia
    potwierdzenie udanej operacji lub blad nie udanej operacji

    klasa logowanie z poziomu koszyka
    wybranie miejsca do wpisania loginu
    wybranie miejsca do wpisania hasla
    wybranie przycisku do zatwierdzenia
    potwierdzenie udanej operacji lub blad nie udanej operacji


    do klasy przekazujemy strone z ktorej nastepuje logowanie

    #zastosowac polimorfizm na tym logowaniu na dwoch roznych stronach
    #uzyc tej klasy logowania (moze byc szukania) do testu tej funckjoncalnosci



    def test_valid_login(self):
        urls = {"https://north.pl/twoje-konto/logowanie",
                "https://north.pl/twoje-zakupy/logowanie-do-sklepu"}
        assert self.driver.current_url in urls



    def test_invalid_login(self):
        pass


@pytest.mark.parametrize("url", ["https://north.pl"]) #, "https://test.north.pl"])
class TestHappyPaths(BaseTest):

    def test_customer_buy_item_from_search_pay_online_with_paczkomaty_no_login(self, url):
        self.homePage = HomePage(self.driver)
        self.homePage.open(url)
        self.homePage.search(item)
        self.articlePage = ArticlePage(self.driver)
        #check what side are we on - article, search group, search list
        #if search group we go to specific iteam
        #if article we go to add to basket
        #if search list we choose specific iteam
        self.articlePage.add_to_basket()
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
        self.homePage.wait_for_suggester(item)

    @pytest.mark.skip
    def test_customer_buy_item_from_search_by_enter_pay_online_with_paczkomaty_no_login(self, url):
        self.homePage = HomePage(self.driver)
        self.homePage.open(url)
        self.homePage.search_by_enter(item)

    @pytest.mark.skip
    def test_main_functions_are_working(self, url):
        self.homePage = HomePage(self.driver)
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
