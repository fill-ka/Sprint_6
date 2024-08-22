from pages.home_page import HomePage
import pytest
import allure
import locators.question_locators as loc
from locators.url import url
from locators.answer_tekst import *

class TestListQuestions:

    @allure.title('Проверка видимости ответов на вопросы')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer', [
        (loc.question_1, loc.answer_1, answer_1),
        (loc.question_2, loc.answer_2, answer_2),
        (loc.question_3, loc.answer_3, answer_3),
        (loc.question_4, loc.answer_4, answer_4),
        (loc.question_5, loc.answer_5, answer_5),
        (loc.question_6, loc.answer_6, answer_6),
        (loc.question_7, loc.answer_7, answer_7),
        (loc.question_8, loc.answer_8, answer_8)
    ])
    def test_question(self, question_locator, answer_locator, expected_answer, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        actual_answer = home_page.search_question_and_open_answer(question_locator, answer_locator)
        assert actual_answer == expected_answer
