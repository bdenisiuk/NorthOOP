from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

wait_time = 30

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator)).click()