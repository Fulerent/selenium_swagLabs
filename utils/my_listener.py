from selenium.webdriver.support.events import AbstractEventListener


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(f'\n========= Ищем элемент. Тип селектора: {by} ', f'Путь до элемента: {value} =========')

    def after_find(self, by, value, driver):
        pass
        print(f"========= Элемент {value} - найден! =========")

    def before_click(self, element, driver):
        print(f"\n========= Кликаем по элементу - {element} =========")

    def after_click(self, element, driver):
        print(f"\n========= Клик по элементу {element} успешно совершен! =========")

    def before_quit(self, driver):
        print(f"\n========= Выполнения теста закончилось! =========")
        pass