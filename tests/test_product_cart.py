import pytest
import allure
from pages.product_page import ProductCart
from utils.locators import Locators
from utils.url_pages import UrlPages as UP


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка перехода на товар')
@allure.feature("Страница с товарами.")
@allure.title("Авторизуймся. Нажима на картинку товара. Переходим на товар")
def test_1_get_to_product_cart_on_image(browser):
    wd = ProductCart(browser)
    wd.login()
    wd.click_product(Locators.FIRST_CART_PRODUCT_IMAGE_LINK)

    assert browser.current_url == UP.SAUCE_LABS_URL


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка перехода на товар')
@allure.feature("Страница с товарами.")
@allure.title("Авторизуймся. Нажима на заголовок товара. Переходим на товар")
def test_2_get_to_product_cart_on_label(browser):
    wd = ProductCart(browser)
    wd.login()
    wd.click_product(Locators.FIRST_CART_PRODUCT_HEADER_LINK)

    assert browser.current_url == UP.SAUCE_LABS_URL


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка добавления в корзину')
@allure.feature("Страница с товарами.")
@allure.title("Авторизуймся. Нажима на кнопку Купить. Товар добавлен в корзину. Проверяем текстовое обозначения кол-ва.")
def test_3_add_first_position_to_cart(browser):
    wd = ProductCart(browser)
    wd.login()
    wd.add_to_cart_through_button(Locators.ADD_FIRST_PRODUCT_TO_SHOPPINGCART)
    count_product = wd.get_element_text(Locators.COUNT_SHOPPING_CART)

    assert count_product == "1"


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка фильтров.')
@allure.feature("Страница с товарами.")
@allure.title("Авторизуймся. Нажима на кнопку Купить несколько раз. "
              "Товар добавлен в корзину. Проверяем текстовое обозначения кол-ва. "
              "Оно должно быть равно кол-ву добавления в корзину.")
@pytest.mark.parametrize("count", list(range(2, 6)))
def test_4_add_many_position_to_cart(browser, count):
    wd = ProductCart(browser)
    wd.login()
    wd.add_many_product_to_cart(count)
    count_products = wd.get_element_text(Locators.COUNT_SHOPPING_CART)

    assert count_products == count


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка фильтров.')
@allure.feature("Страница с товарами.")
@allure.title("Авторизуймся. По очереди меняем фильтры. Смотрим, какой товар будет первый и проверяем.")
@pytest.mark.parametrize("name_filter_and_product", [("az", "Sauce Labs Backpack"),
                                                     ("za", "Test.allTheThings() T-Shirt (Red)"),
                                                     ("lohi", "Sauce Labs Onesie"), ("hilo", "Sauce Labs Fleece Jacket")])
def test_5_check_filter(browser, name_filter_and_product):
    wd = ProductCart(browser)
    wd.login()
    wd.switch_filter(name_filter_and_product[0])
    product_name_of_site = wd.get_name_first_product()

    assert product_name_of_site == name_filter_and_product[1]








