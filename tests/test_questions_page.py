from pages.questions_page import QuestionsPage
from draft_answers import answers
import pytest
import allure

class TestQuestionsPage:

    @allure.title('Проверка ответов соответствующим открываемым вопросам')
    @allure.description('Через метод параметризации поочередно проверяем соответствие текста ответов вопросам')
    @pytest.mark.parametrize('question', answers)
    def test_click_and_get_answer(self, driver, question):
        number, question = question
        question_page = QuestionsPage(driver)
        question_page.click_cookie()
        question_page.scroll_to_element()
        question_page.wait_for_element_appears()
        question_page.click_and_get_answer(number)
        assert question_page.click_and_get_answer(number).text == question

