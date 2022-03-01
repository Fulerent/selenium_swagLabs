#Запуск тестов локально:
pytest --browser <chrome/firefox> --mode local

#Получение отчетов по тестам:
pytest <suite>  --allure-dir <директория для отчетов>

#Обработка отчетов:
1) скачать Allure и распоковать в нужной директории
2) <путь до allure> serve <путь до папки с отчетами>

#Настройка и запуск тестов на Selenoid:
1) https://github.com/aerokube/cm/releases/tag/1.8.1 
скачать от сюда последнию версию менеджера и разместить локально
2) Запустить в папке где лежит exe сам Selenoid
cm.exe selenoid start --vnc
3) Запустить UI
cm.exe selenoid-ui start
4) команда запуска 
pytest <suite> --selenoid <url> 
5) для запуска несколько потоков
pytest <suite> --selenoid <url> -n <кол-во потоков>
