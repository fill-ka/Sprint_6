from pages.home_page import HomePage
import pytest
import allure
import locators.question_locators as loc
from locators.url import url

class TestListQuestions:

    @allure.title('Проверка видимости ответов на вопросы')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer', [
        (loc.question_1, loc.answer_1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (loc.question_2, loc.answer_2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (loc.question_3, loc.answer_3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (loc.question_4, loc.answer_4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (loc.question_5, loc.answer_5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (loc.question_6, loc.answer_6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (loc.question_7, loc.answer_7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (loc.question_8, loc.answer_8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    def test_question(self, question_locator, answer_locator, expected_answer, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        actual_answer = home_page.search_question_and_open_answer(question_locator, answer_locator)
        assert actual_answer == expected_answer
