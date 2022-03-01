import allure
from pages.base_page import BasePage
from utils.locators import Locators
from selenium.webdriver.common.by import By


class ProductCart(BasePage):
    @allure.step('Входим под стандартным юзером')
    def login(self):
        self.login_standard_user()

    @allure.step('Добавляем товар в корзину.')
    def add_to_cart_through_button(self, locator):
        self.find_element(locator).click()

    @allure.step('Добавляем множество товаров в корзину.')
    def add_many_product_to_cart(self, count):
        for i in range(1, count):
            self.add_to_cart_through_button((By.ID, Locators.ADD_PRODUCT_TO_SHOPPINGCART))

    @allure.step('Меняем фильтр на странице товаров.')
    def switch_filter(self, name_filter):
        filters = {"az": Locators.FILTER_A_to_Z,
                   "za": Locators.FILTER_Z_to_A,
                   "lohi": Locators.FILTER_PRICE_LOW_to_HIGH,
                   "hilo": Locators.FILTER_PRICE_HIGH_to_LOW
                   }

        self.find_element(Locators.OPEN_SWITCH_FILTER_MENU).click()
        self.find_element(filters[name_filter]).click()

    @allure.step('Нажимаем на элементм.')
    def go_to_link(self, locator):
        self.find_element(locator).click()

    @allure.step('Получаем имя 1-го товара на странице товаров.')
    def get_name_first_product(self):
        return self.get_element_text_from_list(Locators.FIRST_NAME_PRODUCT)

    @allure.step('Нажимаем на продукт.')
    def click_product(self, locator):
        self.find_element(locator).click()





