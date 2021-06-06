from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

WAIT_TIME = 30
# TODO: seperate PageHeader and PageFooter


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, site):
        self.driver.get(site)
        return self

    def click(self, by_locator):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, WAIT_TIME).until(EC.element_to_be_clickable(by_locator)).click()
        return self

    def wait_for_clickable(self, by_locator):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, WAIT_TIME).until(EC.element_to_be_clickable(by_locator))
        return self


    def element_is_clickable(self, by_locator):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.element_to_be_clickable(by_locator))


    def enter_text(self, by_locator, text):
        if 'ą' in text:
            action = ActionChains(self.driver)
            action.click(self.driver.find_element(*by_locator))
            action.send_keys(text)
            action.perform()
        else:
            return WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
