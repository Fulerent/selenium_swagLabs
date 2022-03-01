import pytest
import allure
from pages.authorization import Authorization
from utils.users import Users as US
from utils.url_pages import UrlPages as UP


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка авторизации.")
@allure.title("Авторизуемся и проверяем url.")
def test_1_standart_login_authorization(browser):
    wd = Authorization(browser)
    wd.login_in(US.STANDART_USER, US.PASSWORD)

    assert browser.current_url == UP.AFTER_LOGIN_SUCCESSFULLY_URL

@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка авторизации.")
@allure.title("Авторизуемся под заблоченным пользовалем. Получаем ошибку и проверяем с ожидаемой.")
def test_2_locked_user_authorization(browser):
    wd = Authorization(browser)
    wd.login_in(US.LOCKED_OUT_USER, US.PASSWORD)
    really_text_alert = wd.get_alert()

    assert really_text_alert == "Epic sadface: Sorry, this user has been locked out."


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка авторизации.")
@allure.title("Авторизуемся под дргуими пользователями. Проверяем урл.")
@pytest.mark.parametrize("login_password", [(US.PROBLEM_USER, US.PASSWORD), (US.PERFORMANCE_GLITCH_USER, US.PASSWORD)])
def test_3_other_user_authorization(browser, login_password):
    wd = Authorization(browser)
    wd.login_in(login_password[0], login_password[1])

    assert browser.current_url == UP.AFTER_LOGIN_SUCCESSFULLY_URL


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка выхода из авторизации.")
@allure.title("Авторизуемся под стандартным пользователем. Выходим из авторизации по кнопке logout. "
              "Попадаем на главную старницу.")
def test_4_logout_through_top_menu(browser):
    wd = Authorization(browser)
    wd.login_in(US.STANDART_USER, US.PASSWORD)
    wd.login_out()

    assert browser.current_url == UP.START_LOGIN_URL


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка выхода из авторизации.")
@allure.title("Авторизуемся под стандартным пользователем. Выходим из авторизации "
              "нажимая кнопку back в browser. Попадаем на главную старницу.")
def test_5_logout_through_back_button(browser):
    wd = Authorization(browser)
    wd.login_in(US.STANDART_USER, US.PASSWORD)
    wd.go_back()

    assert browser.current_url == UP.START_LOGIN_URL


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка ошибки авторизации.")
@allure.title("Авторизуемся под несущ. пользователем. Получаем ошибку авторизации. Остаемся на той же странице.")
def test_6_invalid_login_check_url(browser):
    wd = Authorization(browser)
    wd.login_in("invalid_user", "invalid_password")
    really_text_alert = wd.get_alert()

    assert really_text_alert == UP.START_LOGIN_URL


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка ошибки авторизации.")
@allure.title("Авторизуемся под несущ. пользователем. Получаем ошибку авторизации. Проверяем текст ошибки.")
def test_7_invalid_login_check_notification(browser):
    wd = Authorization(browser)
    wd.login_in("invalid_user", "invalid_password")
    really_text_alert = wd.get_alert()

    assert really_text_alert == "Epic sadface: Username and password do not match any user in this service"

@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка страницы авторизации.')
@allure.feature("Проверка получения сообщения об ошибке авторизации.")
@allure.title("Авторизуемся под несущ. пользователем. Получаем ошибку авторизации. Проверяем текст ошибки.")
def test_8_login_in_second_time(browser):
    wd = Authorization(browser)
    wd.login_in("invalid_user", "invalid_password")
    wd.login_in(US.STANDART_USER, US.PASSWORD)

    assert browser.current_url == UP.START_LOGIN_URL




