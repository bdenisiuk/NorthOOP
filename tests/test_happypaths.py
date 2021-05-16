# happy path
# klient wyszukuje lokowke, wrzuca do koszyka, wybiera platnosc online i wysylke paczkomatem, nie zaklada konta

# testy funkcjonalne
# strona glowna (sprawdzamy czy sie zaladowala poprawnie, czy sa widoczne glowne elementy,
# czy wyszukiwarka jest aktywna, czy koszyk pusty)


# *happy paths
import pytest
import unittest
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHappyPaths(BaseTest):

    @pytest.mark.parametrize("url", ["https://north.pl"])
    def test_customer_buy_item_from_search_pay_online_with_paczkomaty_no_login(self, url):
        self.homePage = HomePage(self.driver)
        self.homePage.open(url)

        # homePage.search(item)
        # articlePage.add_to_basket()
        # cartPage.my_cart()
        # cart.go_to_delivery()
        # cart.choose_delivery()
        # cart.choose_payment()
        # cart.go_to_
        # cart.choose_login()
        # cart.go_to_customer_data
        # cart.fill_customer_data()

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
