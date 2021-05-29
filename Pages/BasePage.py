from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

wait_time = 30


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, site):
        self.driver.get(site)

    def click(self, by_locator):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        if 'ą' in text:
            action = ActionChains(self.driver)
            action.click(self.driver.find_element(*by_locator))
            action.send_keys(text)
            action.perform()
        else:
            return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator)).send_keys(text)