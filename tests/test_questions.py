from pages.home_page import HomePage
import allure
import locators.question_locators as loc
from locators.url import url


class TestListQuestions:
    driver = None

    @allure.title('Проверка видимости ответа на вопрос №1')
    def test_question_1(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_1,
                                                           loc.answer_1)
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка видимости ответа на вопрос №2')
    def test_question_2(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_2,
                                                           loc.answer_2)
        assert answer == (
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
            'несколько заказов — один за другим.')

    @allure.title('Проверка видимости ответа на вопрос №3')
    def test_question_3(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_3,
                                                           loc.answer_3)
        assert answer == (
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
            'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
            'суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Проверка видимости ответа на вопрос №4')
    def test_question_4(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_4,
                                                           loc.answer_4)
        assert answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка видимости ответа на вопрос №5')
    def test_question_5(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_5,
                                                           loc.answer_5)
        assert answer == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')

    @allure.title('Проверка видимости ответа на вопрос №6')
    def test_question_6(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_6,
                                                           loc.answer_6)
        assert answer == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                          'кататься без передышек и во сне. Зарядка не понадобится.')

    @allure.title('Проверка видимости ответа на вопрос №7')
    def test_question_7(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_7,
                                                           loc.answer_7)
        assert answer == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все '
                          'же свои.')

    @allure.title('Проверка видимости ответа на вопрос №8')
    def test_question_8(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.open_site(url)
        answer = home_page.search_question_and_open_answer(loc.question_8,
                                                           loc.answer_8)
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'