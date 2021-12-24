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


    def test_check_delivery_time_outcome(self):
        # TODO: rozbudowac o url i ktory item
        # TODO: dziwny przypadek url         # url = "https://north.pl/chemia-gospodarcza,g1823189.html" not working on this one
        # test przycisku 'Sprawdz czas dostawy' :
        # czy jest reakcja na przycisk (zmienia sie opis lub przenosi na inna strone)
        # czy wyswietla sie czas dostawy, sprawdzamy 'tyg' w tekscie
        url = "https://north.pl/worki-prozniowe,g2056308.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        before = self.grouppage.get_text(self.grouppage.CHECK_DELIVERY_TIME1)
        print(before)
        self.grouppage.hover_to(self.grouppage.CHECK_DELIVERY_TIME1)
        time.sleep(2)
        self.grouppage.click(self.grouppage.CHECK_DELIVERY_TIME1)
        time.sleep(7)
        after = self.grouppage.get_text(self.grouppage.DELIVERY_TIME1)
        print(after)
        assert self.driver.current_url == url
        assert 'Sprawdź czas dostawy' == before
        assert before != after
        assert 'tyg' in after


    def test_filter_expand(self):
        # test reakcji na klikniecie WIECEJ
        # oraz reakcja na klikniecie MNIEJ
        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        before = self.grouppage.get_text(self.grouppage.EXPAND_FILTERS)
        print(before)
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
        # TODO: wait for scroll to stop
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
        # TODO: expand and shrink to different tests


    def test_is_filter_marked_filters(self):
        # TODO: check all filters
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
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
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


    def test_is_filter_marked_show_filter_off_button(self):
        # sprawdzenie czy zaznaczenie filtra wyswietla przycisk do wylaczenia filtrowania
        # TODO usuniecie time sleepow
        url = "https://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        self.grouppage.click(self.grouppage.COOKIES)
        self.grouppage.hover_to(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.wait_for_visible(self.grouppage.FILTER_CANCEL_PROSZEK)
        self.grouppage.wait_for_clickable(self.grouppage.FILTER_CANCEL_PROSZEK)
        time.sleep(2)
        self.grouppage.click(self.grouppage.FILTER_CANCEL_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.wait_for_element_to_disappear(self.grouppage.FILTER_CANCEL_PROSZEK)
        # TODO sprawdzenie czy wcisniecie jednego przycisku dziala poprawnie gdy inne filtry sa uzyte


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
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.FILTER_PROSZEK)
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
        time.sleep(2)
        self.grouppage.click(self.grouppage.WYCZYSC_FILTRY)
        self.driver.execute_script("window.scrollTo(0, 600)")  # this is needed to not click chat box
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
        # TODO: wielkie todo


    # fuck
    def test_if_categories_link_are_working(self):
        #TODO wyrzucic check status do funkcji
        #TODO assercje dokonczyc
        url = "http://north.pl/chemia-gospodarcza,g1823189.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        import requests
        links = self.driver.find_elements(By.XPATH, "//a[@href]")
        for link in links:
            if link.get_attribute("href") == 'javascript:;':
                print('bam')
            else:
                r = requests.head(link.get_attribute('href'))
                print(link.get_attribute('href'), r.status_code)




    @pytest.mark.skip
    def test_if_categories_number_is_correct(self):
        pass

    def test_how_many_displayed_items(self):
        # url = "http://north.pl/chemia-gospodarcza,g1823189.html"
        url = "https://north.pl/blachy,g580814.html"
        self.grouppage = GroupPage(self.driver)
        self.grouppage.open(url)
        displayed_items = self.driver.find_elements(*self.grouppage.LISTED_ITEMS)
        print('Ile artykułów jest wyświetlonych', len(displayed_items))
        items = [] * len(displayed_items)
        for num, item in enumerate(displayed_items):

            properties = ['num', 'name', 'price', 'outlet', 'delivery', 'substitute']
            properties[0] = num+1

            name_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.NAME_POSTFIX
            price_pln_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.PRICE_PLN_POSTFIX
            price_gr_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.PRICE_GR_POSTFIX
            delivery_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.DELIVERY_TIME_POSTFIX
            check_delivery_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.CHECK_DELIVERY_TIME_POSTFIX
            delivery_na_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.DELIVERY_TIME_NA_POSTFIX
            outlet_pln_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.OUTLET_PLN_POSTFIX
            outlet_gr_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.OUTLET_GR_POSTFIX
            form_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.FORM_POSTFIX
            substitute_xpath = self.grouppage.ITEM_XPATH + f'[{num+1}]' + self.grouppage.SUBSTITUTE_POSTFIX

            def check_parameter(param):
                match param:
                    case 'name':
                        if self.grouppage.check_exists_by_xpath(name_xpath):
                            name_prop = self.grouppage.get_text((By.XPATH, name_xpath))
                            return name_prop

                    case 'price':
                        if self.grouppage.check_exists_by_xpath(price_pln_xpath):
                            if self.grouppage.check_contains_other_value_than_nothing(price_pln_xpath):
                                price_prop = self.grouppage.get_text((By.XPATH, price_pln_xpath))
                            else:
                                price_prop = 'NA'
                        else:
                            print('=====================')
                            print('=====================')
                            print('=====================')
                            price_prop = 'NA'
                        properties[2] = price_prop

                    case 'outlet':
                        if self.grouppage.check_exists_by_xpath(outlet_pln_xpath):
                            outlet_prop = self.grouppage.get_text((By.XPATH, outlet_pln_xpath))
                        else:
                            outlet_prop = 'NA'
                        properties[3] = outlet_prop

                    case 'delivery':
                        if self.grouppage.check_exists_by_xpath(delivery_xpath):
                            delivery_prop = self.grouppage.get_text((By.XPATH, delivery_xpath))
                        else:
                            if self.grouppage.check_exists_by_xpath(check_delivery_xpath):
                                delivery_prop = self.grouppage.get_text((By.XPATH, check_delivery_xpath))
                            else:
                                if self.grouppage.check_exists_by_xpath(delivery_na_xpath):
                                    delivery_prop = self.grouppage.get_text((By.XPATH, delivery_na_xpath))
                                else:
                                    delivery_prop = 'NA'
                        properties[4] = delivery_prop

                    case 'substitute':
                        if self.grouppage.check_exists_by_xpath(substitute_xpath):
                            substitute_prop = self.grouppage.get_text((By.XPATH, substitute_xpath))
                        else:
                            substitute_prop = 'NA'
                        properties[5] = substitute_prop

            properties[1] = check_parameter('name')
            check_parameter('price')
            check_parameter('outlet')
            check_parameter('delivery')
            check_parameter('substitute')
            items.append(properties)
        print(items)

        for num, item in enumerate(displayed_items):
            print(num+1)
            assert len(items[num][1]) > 1
            assert len(items[num][2]) > 1
            assert len(items[num][3]) > 1
            assert len(items[num][4]) > 1