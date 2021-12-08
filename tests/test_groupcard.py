import time

import pytest

from pages.articlepage import ArticlePage
from pages.homepage import HomePage
from resources.data import *
from pages.cartpage import CartPage
from pages.grouppage import GroupPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

url = "https://north.pl/worki-prozniowe,g2056308.html"
class TestGroupPage(BaseTest):

    @pytest.mark.skip
    def test_check_delivery_time_outcome(self):
        # TODO: rozbudowac o url i ktory item
        # test przycisku 'Sprawdz czas dostawy' :
        # czy jest reakcja na przycisk (zmienia sie opis lub przenosi na inna strone)
        # czy wyswietla sie czas dostawy, sprawdzamy 'tyg' w tekscie
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        before = self.grouppage.get_text(self.grouppage.CHECK_DELIVERY_TIME1)
        print(before)
        self.grouppage.click(self.grouppage.CHECK_DELIVERY_TIME1)
        time.sleep(7)
        after = self.grouppage.get_text(self.grouppage.DELIVERY_TIME1)
        print(after)
        assert self.driver.current_url == url
        assert 'Sprawdź czas dostawy' == before
        assert before != after
        assert 'tyg' in after

    @pytest.mark.skip
    def test_filter_expand(self):
        # test reakcji na klikniecie WIECEJ
        # oraz reakcja na klikniecie MNIEJ
        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        before = self.grouppage.get_text(self.grouppage.EXPAND_FILTERS)
        print(before)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        #TODO: wait for scroll to stop
        time.sleep(2)
        self.grouppage.click(self.grouppage.EXPAND_FILTERS)
        self.driver.execute_script("window.scrollTo(0, 1080)")
        time.sleep(2)
        after = self.grouppage.get_text(self.grouppage.SHRINK_FILTERS)
        print(after)
        self.grouppage.click(self.grouppage.SHRINK_FILTERS)
        time.sleep(2)
        last = self.grouppage.get_text(self.grouppage.EXPAND_FILTERS)
        print(last)
        assert self.driver.current_url == url
        assert 'WIĘCEJ' == before
        assert before != after
        assert 'MNIEJ' == after
        assert before == last
        #TODO: expand and shrink to different tests

    @pytest.mark.skip
    def test_is_filter_marked_filters(self):
        # sprawdzenie czy zaznaczenie filtra odfiltrowuje pozycje
        # czy liczba przy filtrze zgadza sie z prezentowana w nazwie grupy
        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        filter_name_before = str(self.grouppage.get_text(self.grouppage.FILTER_PROSZEK)).split(' ')[0]
        print('filter_name', filter_name_before)
        filter_items_before = str(self.grouppage.get_text(self.grouppage.FILTER_PROSZEK_ITEMS)).lstrip("(").rstrip(")")
        print('filter_items', filter_items_before)
        group_count_before = str(self.grouppage.get_text(self.grouppage.GROUP_COUNT)).lstrip("(").rstrip(" produktów)")
        print('group_count_name', group_count_before)
        self.grouppage.hover_to(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.FILTER_PROSZEK)
        filter_name_after = self.grouppage.get_text(self.grouppage.FILTER_PROSZEK)
        print('filter_name', filter_name_after)
        filter_items_after = str(self.grouppage.get_text(self.grouppage.FILTER_PROSZEK_ITEMS)).lstrip("(").rstrip(")")
        print('filter_items', filter_items_after)
        group_count_after = str(self.grouppage.get_text(self.grouppage.GROUP_COUNT)).lstrip("(").rstrip(" produktów)")
        print('group_count_name', group_count_after)
        assert (filter_name_before, filter_items_before) == (filter_name_after, filter_items_after)
        assert group_count_after == filter_items_before
        # TODO - sprawdzic zaznaczony filtr z kafelkami wyswietlanymi (forma preparatu)

    @pytest.mark.skip
    def test_is_filter_marked_show_filter_off_button(self):
        # sprawdzenie czy zaznaczenie filtra wyswietla przycisk do wylaczenia filtrowania

        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        self.grouppage.hover_to(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.wait_for_visible(self.grouppage.FILTER_CANCEL_PROSZEK)
        self.grouppage.wait_for_clickable(self.grouppage.FILTER_CANCEL_PROSZEK)
        self.grouppage.click(self.grouppage.FILTER_CANCEL_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.wait_for_element_to_disappear(self.grouppage.FILTER_CANCEL_PROSZEK)
        # TODO sprawdzenie czy wcisniecie jednego przycisku dziala poprawnie gdy inne filtry sa uzyte
    @pytest.mark.skip
    def test_is_clear_filters_working(self):
        # Sprawdzenie poprawnosci dzialania przycisku wyczysc filtry
        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        filter_items_before = str(self.grouppage.get_text(self.grouppage.FILTER_PROSZEK_ITEMS)).lstrip("(").rstrip(")")
        print('filter_items', filter_items_before)
        group_count_before = str(self.grouppage.get_text(self.grouppage.GROUP_COUNT)).lstrip("(").rstrip(" produktów)")
        print('group_count_name', group_count_before)
        self.grouppage.hover_to(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.WYCZYSC_FILTRY)
        self.driver.execute_script("window.scrollTo(0, 600)") # this is needed to not click chat box
        time.sleep(2)
        filter_items_after = str(self.grouppage.get_text(self.grouppage.FILTER_PROSZEK_ITEMS)).lstrip("(").rstrip(")")
        print('filter_items', filter_items_after)
        group_count_after = str(self.grouppage.get_text(self.grouppage.GROUP_COUNT)).lstrip("(").rstrip(" produktów)")
        print('group_count_name', group_count_after)
        assert filter_items_before == filter_items_after
        assert group_count_after == group_count_before

    @pytest.mark.skip
    def test_if_filter_with_0_items_exists(self):
        # czy istnieje filtr z iloscia 0 pozycji
        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        filter_items_before = str(self.grouppage.get_text(self.grouppage.FILTER_PROSZEK_ITEMS)).lstrip("(").rstrip(")")
        print('filter_items', filter_items_before)
        group_count_before = str(self.grouppage.get_text(self.grouppage.GROUP_COUNT)).lstrip("(").rstrip(" produktów)")
        print('group_count_name', group_count_before)
        self.grouppage.hover_to(self.grouppage.FILTER_PROSZEK)
        time.sleep(2)
        self.grouppage.click(self.grouppage.EXPAND_FILTERS)
        #TODO: wielkie todo

    @pytest.mark.skip
    #fuck
    def test_if_categories_link_are_working(self):
        url = "http://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        import requests
        links = self.driver.find_elements_by_xpath("//a[@href]")
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)

    @pytest.mark.skip
    def test_if_categories_number_is_correct(self):
        pass

    def test_how_many_displayed_items(self):
        url = "http://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        displayed_items = self.driver.find_elements(*self.grouppage.LISTED_ITEMS)
        print(len(displayed_items))
        for id, item in enumerate(displayed_items, start=1):
            # from selenium.common.exceptions import NoSuchElementException
            #
            # def check_exists_by_xpath(xpath):
            #     try:
            #         self.driver.find_element_by_xpath(xpath)
            #     except NoSuchElementException:
            #         return False
            #     return True


            name_xpath = self.grouppage.ITEM_XPATH + f'[{id}]' + self.grouppage.NAME_POSTFIX
            gen = (print(self.grouppage.ITEM_XPATH + f'[{id}]' + item) for item in displayed_items)
            x = self.driver.find_element(By.XPATH, name_xpath)
            # print(self.grouppage.get_text(x))

            y = self.grouppage.get_text((By.XPATH, name_xpath))

            print(id, y)





