from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import requests

WAIT_TIME = 30

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open(self, url):
        print(f'-> Open site: {url}')
        self.driver.get(url)
        return self

    def click(self, by_locator):
        print(f"-> Click locator: {by_locator}")
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, WAIT_TIME).until(EC.element_to_be_clickable(by_locator)).click()
        return self

    def wait_for_clickable(self, by_locator):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, WAIT_TIME).until(EC.element_to_be_clickable(by_locator))
        return self

    def wait_for_visible(self, by_locator):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        return self

    def wait_for_element_to_disappear(self, by_locator):
        try:
            WebDriverWait(self.driver, WAIT_TIME).until(EC.presence_of_element_located(by_locator))
        except ElementNotVisibleException:
            print('not visible')
        except TimeoutException:
            print('not visible')



    def enter_text(self, by_locator, text):
        if 'ą' in text:
            action = ActionChains(self.driver)
            action.click(self.driver.find_element(*by_locator))
            action.send_keys(text)
            action.perform()
        else:
            return WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def get_value(self, by_locator):
        return WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).get_attribute('value')

    def get_text(self, by_locator, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(by_locator)).text

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element)


    def gather_options_from_dropdown(self, locator):
        #dropdown_list = self.driver.find_elements(locator)
        dropdown_list = self.driver.find_element(By.ID, 'Limit')
        options = dropdown_list.find_elements(By.TAG_NAME, 'option')
        for opt in options:
            print(opt.text)

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element(By.XPATH,xpath)
        except NoSuchElementException:
            return False
        return True

    def check_contains_other_value_than_nothing(self, xpath):
        try:
            self.get_text((By.XPATH, xpath),1)
        except TimeoutException:
            return False
        return True


    def check_http_status(self, by_locator):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
            http_status = requests.get(by_locator, headers=headers, timeout=WAIT_TIME).status_code
            return http_status
        except:
            print("Site doesn't exists")
            return 404