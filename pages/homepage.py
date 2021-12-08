from pages.basepage import BasePage
from pages.headerpage import PageHeader
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from resources.data import *

# TODO - gdzie umieszczac akcje odnosnie danego page'a ? nazwa akcji jako funkcja i wywolanie funkcji z pliku z
#  akcjami ? Jak wtedy pozbyc sie circular import jesli w pliku z akacjami odwolujemy sie z powrotem do zmiennych
#  lokatorow z page'a (przyklad - pageheader actions obslugujacy wyniki wyszukiwania potrzebuje dostepu do zmiennych z homepage'a np. lokalizator przycisku

class HomePageLocators:
    SEARCH_M = (By.ID, "MobileSearchSwitch")
    SEARCH_TEXTBOX_ID = 'SearchText'
    SEARCH_TEXTBOX_M = (By.ID, 'SearchText')
    SEARCH_SUBMIT_BUTTON_M = (By.XPATH, "//button[@type='submit'][contains(@class,'mr-1')]")
    OPEN_WIZARD_M = (By.XPATH, "//div[contains(@class,'offset-mainheader')]/a")
    WIZARD_DEVICE_TYPE_M = (By.XPATH, "//*[@id='DeviceType']//../small")
    WIZARD_MANUFACTURER_M = (By.XPATH, "//*[@id='Manufacture']//../small")
    WIZARD_MODEL_NUMBER_M = (By.XPATH, "//input[@id='search_model']")
    COOKIES = (By.XPATH, "//a[contains(@class,'btn-dark')]")
    WIZARD_SEARCH_GROUPS = (By.XPATH, "//a[@id='mobile-full']")
    MAIN_TILES_ICON = (
        By.XPATH,
        "//div[@class='row m-0']/div[contains(@class,'align-items-md-center')]/a[contains(@class,'col-md-4')]")
    MAIN_TILES_TEXT = (
        By.XPATH,
        "//div[@class='row m-0']/div[contains(@class,'align-items-md-center')]/a[contains(@class,'col-md-8')]")
    HAMBURGER_MENU = (By.XPATH, "//*[@id='menu-switch']")
    HAMBURGER_MENU_FOLD = (By.XPATH, "//*[@id='menu-switch'][contains(@aria-expanded,'false')]")
    HAMBURGER_MENU_UNFOLD = (By.XPATH, "//*[@id='menu-switch'][contains(@aria-expanded,'true')]")
    HAMBURGER_MENU_POSITIONS = (By.XPATH, "//*[@id='menu-switch']/../div/ul/li")

    CAROUSEL_ITEMS = (By.XPATH, "//div[@id='group-crosselling-carousel']//div[contains(@class,'product-item')]/div/div")


    # def HAMBURGER_LIST(menu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]/span"
    #     return (By.XPATH, xpat)
    #
    # def HAMBURGER_SUBMENU_LIST(menu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='submenu-column col-md-4']/span"
    #     return (By.XPATH, xpat)
    #
    # def HAMBURGER_SUBMENU(menu, submenu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='submenu-column col-md-4'][" + \
    #            str(submenu) + "]/span"
    #     return (By.XPATH, xpat)
    #
    # def HAMBURGER_SUBMENU_LINKS_LISTS(menu, submenu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='submenu-column col-md-4'][" + \
    #            str(submenu) + "]/span/../ul/li"
    #     return (By.XPATH, xpat)
    #
    # def HAMBURGER_SUBMENU_LINKS(menu, submenu, submenu_link):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='submenu-column " \
    #                                                                  "col-md-4'][" + str(submenu) + \
    #            "]/span/../ul/li[" + str(submenu_link) + \
    #            "]/a"
    #     return (By.XPATH, xpat)
    #
    # # czesci do laptopa
    # def HAMBURGER_LINK_OUTSIDE_SUBMENU(menu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='submenu-column col-md-4']/../a"
    #     return (By.XPATH, xpat)
    #
    # def HAMBURGER_SUBMENU_PROMO_LINK(menu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='col-md-4 ban']/a/img"
    #     return (By.XPATH, xpat)
    #
    # def HAMBURGER_SUBMENU_PROMO_NAME(menu):
    #     xpat = "//nav[@id='header-bottom']/div/ul/li[" + str(menu) + "]//div[@class='col-md-4 ban']/a"
    #     return (By.XPATH, xpat)
    #
    # def promo_item(part, position='1'):
    #     base = "//div[contains(@class,'promo-product')]//div[contains(@class,'product-item')]"
    #     photo = "//a[contains(@class,'product-item-foto')]"
    #     info = "//div[contains(@class,'product-info')]/a"
    #     price = "//span[contains(@class,'product-price')]"
    #     delivery = "//small[contains(@class,'product-delivery')]"
    #
    #     image = "/img"
    #     # tylko na potrzeby znalezienie webelementu dla action chains
    #     # test z karuzela promocyjnych produktow na stronie glownej
    #
    #     if part == 'photo':
    #         xpat = '(' + base + photo + ')[' + str(position) + ']'
    #     elif part == 'info':
    #         xpat = '(' + base + info + ')[' + str(position) + ']'
    #     elif part == 'price':
    #         xpat = '(' + base + price + ')[' + str(position) + ']'
    #     elif part == 'delivery':
    #         xpat = '(' + base + delivery + ')[' + str(position) + ']'
    #     elif part == 'image':
    #         xpat = '(' + photo + image + ')[' + str(position) + ']'
    #     elif part == 'base':
    #         xpat = '(' + base + ')[' + str(position) + ']'
    #
    #     if position == 0:
    #         xpat = base
    #     return (By.XPATH, xpat)
    #
    # "//a[@class='d-flex align-items-center justify-content-center my-3 product-item-foto']/img)["
    #
    # promo_active_items = (
    #     By.XPATH, "//div[@id='group-crosselling-carousel']/div/div/div[contains(@class,'slick-active')]")
    # promo_next_arrow = (By.XPATH, "//button[@class='slick-next slick-arrow']")
    # promo_prev_arrow = (By.XPATH, "//button[@class='slick-prev slick-arrow']")
    #
    # SEARCH_TEXTBOX = (By.ID, "SearchText")
    # SEARCH_SUBMIT_BUTTON = (By.XPATH, "//input[@id='SearchText']/../button")
    # # SEARCH_SUBMIT_BUTTON = (By.XPATH, "//input[@id='SearchText']/following-sibling::button")
    # WIZARD_DEVICE_TYPE = (By.ID, "wizzart-device-list")
    # WIZARD_MANUFACTURER = (By.ID, "wizzart-brand-list")
    #
    # def wizard_manufacturer_brand(brand):
    #     return (By.XPATH, "//div[@id='wizzart-brand-list']//div[@id='urz_list']//a[contains(text(),'" + brand + "')]")
    #
    # def wizard_device_type(device): return (By.XPATH, "//div[@id='wizzart-device-list']//div[@id='urz_list']//a[
    # contains(text(),'" + device + "')]")
    #
    # WIZARD_MANUFACTURER_CHECK = (By.XPATH, "//div[@id='wizzart-brand-list']//./span/span")
    #
    # WIZARD_DEVICE_TYPE_CHECK = (By.XPATH, "//div[@id='wizzart-device-list']//./span/span")
    # WIZARD_MODEL_CHECK = (By.XPATH, "//div[@id='model_search']/input[contains(@class,'search_input')]")
    #
    # WIZARD_MODEL_NUMBER = (By.ID, "search_model")
    # WIZARD_SEARCH_BUTTON = (By.ID, "search_btn")
    # WIZARD_HELP = (By.ID, "wizard_help_switch")
    # BASKET = (By.ID, 'koszyk_status')
    # BASKET_COUNT = (By.XPATH, "//div[@id='koszyk_status']/a/i")
    # LOGIN = (By.XPATH, "//div[@id='login_status']/a")
    # LOGIN_BUTTON = (By.XPATH, "//div[@id='login_status']//a[contains(@class,'btn')]")


class HomePage(BasePage):

    COOKIES = (By.XPATH, "//*[@id='cookies-info']//a[contains(@class,'btn')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = PageHeader(self.driver)

    def search(self, search_phrase, click_enter=False):
        self.header.enter_search_phrase(search_phrase)
        if click_enter:
            self.header.send_enter_to_search_form()
        else:
            self.header.click_search_button()
        print(f'tutaj jestem', self.driver.current_url)
        return self.header.actions.check_search_result(self.driver.current_url)


    def wait_for_suggester(self, search_phrase):
        self.header.wait_for_suggester(search_phrase)

    def main_functions_are_working(self):
        search_textbox = self.driver.find_element(SEARCHED_ITEM)
        search_textbox.is_displayed()
        search_icon = self.driver.find_element(SEARCHED_ITEM)
        search_icon.is_displayed()

    # wyszukiwarka
    # wizard
    # kafelki glowne
    # wyswietlanie grafik glownych
    # karuzela_artykulow
    # karuzela_marek
    # menu
    #
    #
    # search.is_visible()
    # search.display_inserted_text
    # search.activated_by_click
    # search.activated_by_enter
    # search.move_to_other_site
    # search.display_suggester

    # def search(self, search_term):
    #     self.driver.find_element(*HomePageLocators.SEARCH_TXT).clear()
    #     self.enter_text(HomePageLocators.SEARCH_TXT, search_term)
    #     self.click(HomePageLocators.search_submit_btn)
