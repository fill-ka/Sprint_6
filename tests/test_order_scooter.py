from pages.order_scooter import OrderPage
import pytest
import allure
from locators.url import url
from locators.order_test_data import date, comment

class TestOrderScooter:

    @allure.title('Проверка успешного заказа самоката по клику на кнопку "Заказать" вверху страницы')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Анна', 'Комова', 'Сокол', '89254622860', 'Ул. Тверская, д.10'],
                              ['Юлия', 'Галкина', 'Спартак', '89250659797', 'Ул. Летчика Бабушкина, д.2']])
    def test_order_button_top(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.open_and_accept_cookies(url)
        order_page.order_via_top_button(name, surname, address, phone_number, metro, date, comment)
        assert order_page.verify_return_to_main_page()

    @allure.title('Проверка успешного заказа самоката по клику на кнопку "Заказать" внизу страницы')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Арсен', 'Куликов', 'Южная', '89165329765', 'Ул. 1905 года, д.98'],
                              ['Егор', 'Воловик', 'Коньково', '89153276263', 'Ул. Арбатская, д.3']])
    def test_order_button_below(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.open_and_accept_cookies(url)
        order_page.order_via_bottom_button(name, surname, address, phone_number, metro, date, comment)
        assert order_page.verify_order_success()

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип «Самоката»')
    def test_logo_scooter_redirect(self, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.open_and_accept_cookies(url)

        order_page.verify_return_to_main_page()

        assert 'Самокат' in order_page.get_element_text(order_page.header_scooter_main)

    @allure.title('Проверка открытия главной страницы Дзена в новом окне при нажатии на логотип Яндекса')
    def test_logo_yandex_redirect(self, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.open_and_accept_cookies(url)

        order_page.click_element(order_page.logo_yandex_main)

        order_page.switch_to_new_window()

        order_page.wait_for_element_visible(order_page.dzen_main_page_header)

        assert 'dzen.ru' in order_page.get_current_url()
