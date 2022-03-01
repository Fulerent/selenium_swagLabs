from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_element_text(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}").text

    def get_element_text_from_list(self, locator, time=5, position=0):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")[position].text

    def go_to_source(self, url):
        return self.driver.get(url)

    def go_back(self):
        return self.driver.back()

    def login_standard_user(self):
        self.find_element(Locators.USER_INPUT).send_keys("standard_user")
        self.find_element(Locators.PASSWORD_INPUT).send_keys("secret_sauce")
        self.find_element(Locators.LOGIN_BUTTON).click()

        return self
