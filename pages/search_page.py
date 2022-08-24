from .base_page import BasePage
from .locators import SearchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    # Проверить наличие поля поиска
    def should_be_search_form(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_FORM), "Search form is not presented"

    # Ввести в поиск Совкомбанк
    def enter_in_search(self, query):
        search_field = self.browser.find_element(*SearchPageLocators.SEARCH_FORM)
        search_field.send_keys(query)

    # Проверить, что появилась таблица с подсказками
    def should_be_hint_table(self):
        assert self.is_element_present(*SearchPageLocators.HINT_TABLE), "Hint table is not presented"

    # Проверить, что в вариантах подсказок есть слово совкомбанк
    def should_be_query_in_hint_table(self):
        assert self.is_element_present(*SearchPageLocators.WORD_IN_HINTS), "Word is not presented"

    # Выполнить поиск (Нажать ENTER)
    def run_search_enter(self):
        search_field = self.browser.find_element(*SearchPageLocators.SEARCH_FORM)
        search_field.send_keys(Keys.ENTER)

    # Выполнить поиск (Нажать кнопку Поиск в Google)
    def run_search_button(self):
        search_button = self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_button_clickable = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(search_button))
        search_button_clickable.click()

    # Проверить появление результатов
    def should_be_search_results_table(self):
        search_results = self.browser.find_elements(*SearchPageLocators.SEARCH_RESULTS)
        result_count = len(search_results)
        assert result_count > 0, "No search results"

    # Проверить, есть ли в первых 5 результатах поиска ссылка на sovcombank.ru
    # Вывести в каких по счету результатах ссылка не найдена, если таковые имеются
    # Под единицей результата подразумевались отделно выдаваемые блоки с информацией относящейся только к этому блоку
    # Ддополнительные ссылки в блоке не брались за самостоятельную единицу результата, но учитывались при поиске ссылки в блоке
    def should_be_links_to_sovcom(self):
        without_links = []
        sample_of_results = 5
        link_to = "sovcombank.ru"
        for i in range(1, sample_of_results + 1):
            locator = "//*[@id='rso']/div[" + str(i) + "]//a[contains(@href,'" + link_to + "')]"
            if self.is_element_present(By.XPATH, locator) == False:
                without_links.append(i)
        assert len(without_links) == 0, "The following results without links to sovcom: " + str(without_links)

    # Проверить, что кнопка «Картинки» присутствует на странице
    def should_be_pictures_button(self):
        assert self.is_element_present(*SearchPageLocators.PICTURES_BUTTON), "Pictures button is not presented"

    # Нажать на кнопку «Картинки»
    def press_pictures_button(self):
        link = self.browser.find_element(*SearchPageLocators.PICTURES_BUTTON)
        link.click()
