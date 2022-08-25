# task

Тестирование реализовано на Python3 + Selenium Webdriver с применением паттерна Page Objects Model.

Тест сценария 1: 
```
pytest -s -v test_search.py
```

Тест сценария 2:
```
pytest -s -v test_pictures.py
```

Chrome:
```
pytest --browser_name=chrome
```

Firefox:
```
pytest --browser_name=firefox
```

Сторонние библиотеки: pytest, allure-pytest.

```
pip install pytest

pytest -s -v
```

```
pip install allure-pytest

pytest -s -v --alluredir=allureress

allure serve allureress
```
