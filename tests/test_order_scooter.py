from pages.order_scooter import OrderPage
import pytest
import allure
import locators.order_locators as loc
from locators.url import url
from locators.order_test_data import date, comment


class TestOrderScooter:
    driver = None

    @allure.title('Проверка успешного заказа самоката по клику на кнопку "Заказать" вверху страницы')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Анна', 'Комова', 'Сокол', '89254622860', 'Ул. Тверская, д.10'],
                              ['Юлия', 'Галкина', 'Спартак', '89250659797', 'Ул. Летчика Бабушкина, д.2']])
    def test_order_button_top(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.open_site(url)
        order_page.click_cookie_button(loc.button_accept_cookies)

        order_page.wait_and_click(loc.button_order_small)
        order_page.fill_customer_info(loc.input_name, name, loc.input_surname, surname, loc.input_address, address,
                                      loc.input_phone, phone_number, loc.input_metro_station, metro)

        order_page.click_and_wait_for_element(loc.button_next_step, loc.header_about_rent)
        order_page.fill_rental_info(loc.dropdown_rent_duration, loc.option_one_day, loc.checkbox_black_scooter,
                                    loc.input_rent_date, date, loc.input_comment, comment)

        order_page.confirm_order(loc.button_order_medium, loc.button_confirm_yes, loc.button_check_status)

        order_page.click_element(loc.logo_main_scooter)
        order_page.wait_for_element_visible(loc.header_scooter_main)

        assert 'на пару дней' and 'Самокат' in order_page.get_element_text(loc.header_scooter_main)

    @allure.title('Проверка успешного заказа самоката по клику на кнопку "Заказать" внизу страницы')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Арсен', 'Куликов', 'Южная', '89165329765', 'Ул. 1905 года, д.98'],
                              ['Егор', 'Воловик', 'Коньково', '89153276263', 'Ул. Арбатская, д.3']])
    def test_order_button_below(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.open_site(url)

        order_page.click_cookie_button(loc.button_accept_cookies)
        order_page.scroll_and_click(loc.button_order_large)
        order_page.fill_customer_info(loc.input_name, name, loc.input_surname, surname, loc.input_address, address,
                                      loc.input_phone, phone_number, loc.input_metro_station, metro)

        order_page.click_and_wait_for_element(loc.button_next_step, loc.header_about_rent)
        order_page.fill_rental_info(loc.dropdown_rent_duration, loc.option_one_day, loc.checkbox_black_scooter,
                                    loc.input_rent_date, date, loc.input_comment, comment)

        order_page.click_element(loc.button_order_medium)
        order_page.click_element(loc.button_confirm_yes)

        assert "Заказ оформлен" in order_page.get_element_text(loc.message_order_success)

