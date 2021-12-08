from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select as WebDriverSelect
import time

class GroupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    COOKIES = (By.XPATH, "//a[contains(@class,'btn-dark')]")

    BREADCRUMB_LIST = (By.XPATH, "//li[contains(@class,'breadcrumb')]")
    BREADCRUMB_ACTIVE = (By.XPATH, "//li[contains(@class,'activ breadcrumb')]")
    BREADCRUMB_UPPER = (By.XPATH, "//li[contains(@class,'breadcrumb')][last()-1]")
    GROUP_NAME = (By.XPATH, "//div[contains(@class,'product-list-head')]//div[contains(@class,'h1')]/h1")
    GROUP_COUNT = (By.XPATH, "//div[contains(@class,'product-list-head')]//div[contains(@class,'h1')]/span")
    DDL_FILTER_ITEMS = (By.ID, "Limit")


    # ITEM PROPERTIES
    ITEM_XPATH = "//*[@id='prodict-tin-contener']/*[contains(@class,'product-item')]"
    LISTED_ITEMS = (By.XPATH, ITEM_XPATH)
    NAME_POSTFIX = "//div[@class='product-info']/a"
    PRICE_PLN_POSTFIX = "//div[contains(@class,'product-price')]//span"
    PRICE_GR_POSTFIX = "//div[contains(@class,'product-price')]//span/sup"
    DELIVERY_TIME_POSTFIX = "//*[contains(@class,'product-delivery')]/span"
    CHECK_DELIVERY_TIME_POSTFIX = "//*[contains(@class,'product-delivery')]/a/u"
    OUTLET_PLN_POSTFIX = "//*[@class='mt-3 text-muted']"
    OUTLET_GR_POSTFIX = "//*[@class='mt-3 text-muted']/sup"
    FORM_POSTFIX = "//div[@class='mt-3']/div/span"
    SUBSTITUTE_POSTFIX = "//div[contains(@class,'ps-3')]/a"

    DELIVERY_TIME = (By.XPATH, "//*[@id='prodict-tin-contener']//small[contains(@class,'product-delivery')]/span")
    CHECK_DELIVERY_TIME = (By.XPATH, "//*[contains(@class,'product-delivery')]/*[@id='check-delivery-time']")
    # CHECK_DELIVERY_TIME1= (By.XPATH, "(//*[contains(@class,'product-delivery')]/*[@id='check-delivery-time'])[1]")
    CHECK_DELIVERY_TIME1= (By.XPATH, "(//*[contains(@class,'product-delivery')]/a/u[text()='Sprawdź czas dostawy'])[1]")
    DELIVERY_TIME1= (By.XPATH, "//*[@id='prodict-tin-contener']/*[contains(@class,'product-item')][1]//*[contains(@class,'product-delivery')]/span")

    # Filters
    FILTERS = (By.ID, 'filters')
    FILTERS_GROUP_NAME = (By.XPATH, "//*[@id='filters']/span[contains(@class,'h6')]")
    FILTERS_POSITIONS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/div")
    # EXPAND_FILTERS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/a[text()='WIĘCEJ']")
    EXPAND_FILTERS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/a")

    SHRINK_FILTERS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/a")
    FILTERS_UNHIDED_POSITIONS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/div[contains(@class,'d-all')]")
    FILTERS_HIDED_POSITIONS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/div[not(contains(@class,'d-all'))]")
    FILTER_PROSZEK = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/div/label[contains(text(),'proszek')][1]")
    FILTER_PROSZEK_ITEMS = (By.XPATH, "//*[@id='filters']/div[@class=' bg-light p-3']/div/label[contains(text(),'proszek')]/span")
    FILTER_CANCEL_PROSZEK = (By.XPATH, "//div[@id='parameter-remove']/a/span[contains(text(),'proszek')]")
    WYCZYSC_FILTRY = (By.XPATH, "//div[@id='filter-btn']/a[contains(text(),'Wyczyść filtry')]")

    def check_site(self):
        assert ',g' in self.driver.current_url

    def displayed_items(self):
        items = self._count_displayed_items()
        displayed_items=[]
        name_xpath_postfix = "//div[@class='product-info']/a"
        price_pln_xpath_postfix = "//div[contains(@class,'product-price')]//span"
        price_gr_xpath_postfix = "//div[contains(@class,'product-price')]//span/sup"
        delivery_time_xpath_postfix = "//*[contains(@class,'product-delivery')]/span"
        check_delivery_time_xpath_postfix = "//*[contains(@class,'product-delivery')]/a/u"
        outlet_pln_xpath_postfix = "//*[@class='mt-3 text-muted']"
        outlet_gr_xpath_postfix = "//*[@class='mt-3 text-muted']/sup"
        print(type(name_xpath_postfix))
        print(type(items))
        print(items)
        for id, item in enumerate(range(items), start=1):
            item_xpath_for_id = self.ITEM_XPATH + '[' + str(id) + ']'
            xpath = item_xpath_for_id + name_xpath_postfix
            print(xpath)
            name = self.driver.find_element(By.XPATH, xpath)
            print(self.get_text(name))

            # name = self.driver.find_element(By.XPATH, item_xpath_for_id + name_xpath_postfix)
            #promo_items = self.driver.find_element(By.XPATH, item_xpath_for_id + promo_i)
            #outlet_items = self.driver.find_element(By.XPATH, str(item_xpath_for_id) + str(outlet_pln_xpath_postfix))
            print(name) #, outlet_items)

        #     NA_items =
            #items_with_substitute
        #     items_with_offer
        # # item1=[name,price, delivery_time, other]
        # other = old price, substitute, offer, promo]


        return list

    # TODO click if possible
    def breadcrumb_up(self):
        self.click(self.BREADCRUMB_UPPER)

    def number_of_items_in_group_name(self):
        items = (self.get_text(self.GROUP_COUNT)).lstrip("(").rstrip(" produktów)")
        return items


    def change_number_of_displayed_items(self, option):
        self.gather_options_from_dropdown(self.DDL_FILTER_ITEMS)
        dropdown = self.driver.find_element(*self.DDL_FILTER_ITEMS)
        select_list = WebDriverSelect(dropdown)
        select_list.select_by_value(option)

    def _count_displayed_items(self):
        return len(self.driver.find_elements(*self.LISTED_ITEMS))

    def read_delivery_time(self):
        return self.get_text(self.DELIVERY_TIME)

    def check_delivery_time_clickable(self):
        url = self.driver.current_url
        self.wait_for_clickable(self.CHECK_DELIVERY_TIME)
        self.hover_to(self.CHECK_DELIVERY_TIME)
        check_delivery_time = self.get_text(self.CHECK_DELIVERY_TIME)
        print(check_delivery_time)
        self.click(self.CHECK_DELIVERY_TIME)
        time.sleep(5)
        delivery_time = self.get_text(self.CHECK_DELIVERY_TIME)
        print(delivery_time)
        print(check_delivery_time)






    # breadcrumb - czy dzialaja linki, czy sa w jednej lini, czy poziom wyzszy jest poziomem wyzszym, czy menu z lewej koreluje z poziomem breadcrumba
    # menu z lewej - czy linki dzialaja, czy ilosc artykulow sie zgadza, czy suma z grupy sie zgadza, czy przejscie gora/dol/powrot dziala
    # menu z lewej - filtry czy dzialaja,
    # nazwa grupy czy zgadza sie url
    # ilosc produktow czy zgadza sie z ta z menu, czy zgadza sie z iloscia wyswietlana
    # filtry wyswietlania pozycji, filtrowanie wedlug ceny
    # artykuly - akcje na kafelku- oddzielny modul,4 pewniaki sprawdzanie cen (api/sql/strona art),


