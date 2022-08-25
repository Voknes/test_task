from .base_page import BasePage
from .locators import PicturesPageLocators

class PicturesPage(BasePage):
    # Открыть вторую картинку
    def open_second_image(self):
        link = self.browser.find_element(*PicturesPageLocators.SECOND_IMAGE_LINK)
        link.click()

    # Проверить, что картинка открылась и вернуть ее src
    def should_be_second_image_on_page(self):
        assert self.is_element_present(*PicturesPageLocators.CURRENT_IMAGE), "Image is not presented"
        second_image = self.browser.find_element(*PicturesPageLocators.CURRENT_IMAGE).get_attribute("src")
        return second_image

    # Нажатие кнопки Вперед
    def press_next_button(self):
        next_button = self.browser.find_element(*PicturesPageLocators.NEXT_BUTTON)
        next_button.click()

    # После нажатия кнопки Вперед картинка изменилась
    def should_be_image_changed_after_press_next_button(self, second_image):
        current_image = self.browser.find_element(*PicturesPageLocators.CURRENT_IMAGE).get_attribute("src")
        assert second_image != current_image, "Image has not changed"

    # Нажатие кнопки Назад
    def press_prev_button(self):
        prev_button = self.browser.find_element(*PicturesPageLocators.PREV_BUTTON)
        prev_button.click()

    # Проверить, что картинка изменилась на картинку из шага 4
    def should_be_image_changed_after_press_prev_button(self, second_image):
        current_image = self.browser.find_element(*PicturesPageLocators.CURRENT_IMAGE).get_attribute("src")
        assert second_image == current_image, "Image not from step 4"
