from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    URL = "https://north.pl/twoje-konto/logowanie"

    EMAIL = (By.ID, "LoginName")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[contains(@class,'btn')]")
    # FORGET PASSWORD