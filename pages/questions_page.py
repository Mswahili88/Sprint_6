from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class QuestionsPage(BasePage):

    QUESTION_1 = (By.ID, "accordion__heading-0")
    ANSWER_1 = (By.ID, "accordion__panel-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    ANSWER_8 = (By.ID, "accordion__panel-7")

    @allure.step('Ищем вопросы, раскрываем их и фиксируем ответы')
    def click_and_get_answer(self, number):
        self.wait_and_find_element(self.question_locator(number)).click()
        return self.wait_and_find_element(self.answer_locator(number))

    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self):
        self.scroll(self.QUESTION_1)

    @allure.step('Ожидаем появления элемента, до которого скроллили')
    def wait_for_element_appears(self):
        self.wait_and_find_element(self.QUESTION_1)



