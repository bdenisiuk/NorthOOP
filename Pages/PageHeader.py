from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class PageHeader(BasePage):

    def __init__(self, driver):
        self.driver = driver

    class Wizard():

        def __init__(self, driver):
            self.driver = driver
            super().__init__(driver)

        wizard_device_ddl = (By.ID, "wizzart-device-list")
        wizard_mfg_ddl = (By.ID, "wizzart-brand-list")
        wizard_model_txt = (By.ID, "search_model")


        def wizard_manufacturer_brand(brand):
            return (
            By.XPATH, "//div[@id='wizzart-brand-list']//div[@id='urz_list']//a[contains(text(),'" + brand + "')]")

        def wizard_device_type(device):
            return (
            By.XPATH, "//div[@id='wizzart-device-list']//div[@id='urz_list']//a[contains(text(),'" + device + "')]")

        WIZARD_MANUFACTURER_CHECK = (By.XPATH, "//div[@id='wizzart-brand-list']//./span/span")

        WIZARD_DEVICE_TYPE_CHECK = (By.XPATH, "//div[@id='wizzart-device-list']//./span/span")
        WIZARD_MODEL_CHECK = (By.XPATH, "//div[@id='model_search']/input[contains(@class,'search_input')]")

        WIZARD_MODEL_NUMBER = (By.ID, "search_model")
        WIZARD_SEARCH_BUTTON = (By.ID, "search_btn")
        WIZARD_HELP = (By.ID, "wizard_help_switch")

        def wizard_is_active(self):
            pass
