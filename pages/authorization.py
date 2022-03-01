import time
import allure
from pages.base_page import BasePage
from utils.locators import Locators


class Authorization(BasePage):
    @allure.step('Входим под юзером - {user} и пароль - {password}.')
    def login_in(self, user, password):
        self.find_element(Locators.USER_INPUT).send_keys(user)
        self.find_element(Locators.PASSWORD_INPUT).send_keys(password)
        self.find_element(Locators.LOGIN_BUTTON).click()

    @allure.step('Выходим из сеанса.')
    def login_out(self):
        self.find_element(Locators.OPEN_TOP_MENU).click()
        time.sleep(1)
        self.find_element(Locators.LOGOUT_LINK).click()

    @allure.step('Получаем текст нотификации.')
    def get_alert(self):
        return self.get_element_text(Locators.ERROR_MESSAGE)






