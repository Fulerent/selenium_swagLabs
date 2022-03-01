import pytest
import allure
import json
from selenium import webdriver
from utils.url_pages import UrlPages as UP


def pytest_addoption(parser):
    parser.addoption('--browser', action='store',
                     default='chrome')
    parser.addoption('--mode', action='store',
                     default='selenoid')
    parser.addoption('--url', action='store',
                     default=f'{UP.START_LOGIN_URL}')
    parser.addoption('--selenoid', action='store',
                     default='localhost')


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("--browser")
    selenoid = request.config.getoption('--selenoid')
    mode = request.config.getoption('--mode')

    if mode == 'selenoid':
        execution_url = f'http://{selenoid}:4444/wd/hub'

        caps = {
            "browserName": browser,
            "browserVersion": "98.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        driver = webdriver.Remote(command_executor=execution_url, desired_capabilities=caps)
    elif mode == 'local':
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.headless = False
            # options.add_argument('start-fullscreen')
            driver = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.headless = True
            options.add_argument('start-fullscreen')
            driver = webdriver.Firefox(options=options)
        else:
            raise Exception("Такой браузер не поддерижвается")
    else:
        raise Exception(f"Такой --mode - {mode} не поддерживается. Введите local/selenoid")

    session_id = driver.session_id

    allure.attach(name=session_id,
                  body=json.dumps(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)
    driver.get(UP.START_LOGIN_URL)
    yield driver

    print("\nquit browser..")
    driver.quit()
