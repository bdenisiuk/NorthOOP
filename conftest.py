import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture(params=['chrome', 'firefox'], scope='class')
@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # chrome_options.headless = True
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    if request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

    request.cls.driver = driver
    driver.set_window_size(1920, 1080)
    driver.maximize_window()

    yield
    driver.close()
    driver.quit()
