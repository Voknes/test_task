from .pages.search_page import SearchPage
import pytest

url = "https://www.google.com/"
query = "Совкомбанк"

class TestSearchInGoogle():
    # Проверка на наличие поля поиска
    def test_guest_should_see_search_form_on_main_page(self, browser):
        link = url
        page = SearchPage(browser, link)
        page.open()
        page.should_be_search_form()

    # Проверка на ввод в поиск, появление таблицы подсказок, наличие слова совкомбанк в подсказках
    def test_guest_can_enter_in_search(self, browser):
        link = url
        page = SearchPage(browser, link)
        page.open()
        page.enter_in_search(query)        
        page.should_be_hint_table()
        page.should_be_query_in_hint_table()

    # Проверка на выполнение поиска нажатием кнопки Поиск в Google и появление результатов
    def test_guest_can_run_search_with_button(self, browser):
        link = url
        page = SearchPage(browser, link)
        page.open()
        page.enter_in_search(query) 
        page.run_search_button()
        page.should_be_search_results_table()
    
    # Проверка на выполнение поиска нажатием ENTER и появление результатов
    def test_guest_can_run_search_with_enter(self, browser):
        link = url
        page = SearchPage(browser, link)
        page.open()
        page.enter_in_search(query)
        page.run_search_enter()
        page.should_be_search_results_table()

    # Проверка на наличие в первых 5 результатах поиска ссылки на sovcombank.ru
    # Под единицей результата подразумевались отделно выдаваемые блоки с информацией относящейся только к этому блоку
    # Дополнительные ссылки в блоке не брались за самостоятельную единицу результата, но учитывались при поиске ссылки в блоке)
    @pytest.mark.xfail
    def test_should_be_links_to_sovcom_in_first_five_results(self, browser):
        link = url
        page = SearchPage(browser, link)
        page.open()
        page.enter_in_search(query)
        page.run_search_enter()
        page.should_be_links_to_sovcom()
