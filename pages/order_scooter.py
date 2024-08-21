import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):

    # Локаторы
    button_order_small = ('locator_type', 'locator_value')
    button_order_large = ('locator_type', 'locator_value')
    input_name = ('locator_type', 'locator_value')
    input_surname = ('locator_type', 'locator_value')
    input_address = ('locator_type', 'locator_value')
    input_metro_station = ('locator_type', 'locator_value')
    input_phone = ('locator_type', 'locator_value')
    button_next_step = ('locator_type', 'locator_value')
    header_about_rent = ('locator_type', 'locator_value')
    input_rent_date = ('locator_type', 'locator_value')
    dropdown_rent_duration = ('locator_type', 'locator_value')
    option_one_day = ('locator_type', 'locator_value')
    checkbox_black_scooter = ('locator_type', 'locator_value')
    input_comment = ('locator_type', 'locator_value')
    button_confirm_yes = ('locator_type', 'locator_value')
    message_order_success = ('locator_type', 'locator_value')
    logo_main_scooter = ('locator_type', 'locator_value')
    header_scooter_main = ('locator_type', 'locator_value')
    button_accept_cookies = ('locator_type', 'locator_value')

    @allure.step("Выбор цвета самоката: {locator}")
    def select_scooter_color(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Заполнение информации о заказчике: имя - {name}, фамилия - {surname}, адрес - {address}, телефон - {phone}, метро - {metro}")
    def fill_customer_info(self, name_locator, name, surname_locator, surname, address_locator, address,
                           phone_locator, phone, metro_locator, metro):
        self.fill_input(name_locator, name)
        self.fill_input(surname_locator, surname)
        self.fill_input(address_locator, address)
        self.fill_input(phone_locator, phone)
        self.wait_for_element_clickable(metro_locator)
        metro_input = self.driver.find_element(*metro_locator)
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    @allure.step("Заполнение информации о прокате: дата - {date}, комментарий - {comment}")
    def fill_rental_info(self, rental_period_locator, period_locator, color_locator, date_locator, date, comment_locator, comment):
        self.fill_input(date_locator, date)
        self.driver.find_element(*date_locator).send_keys(Keys.ENTER)
        self.click_element(rental_period_locator)
        self.click_element(period_locator)
        self.click_element(color_locator)
        self.fill_input(comment_locator, comment)

    @allure.step("Ожидание и клик по элементу: {locator}")
    def wait_and_click(self, locator):
        self.wait_for_element_clickable(locator)
        self.click_element(locator)

    @allure.step("Клик по элементу {click_locator} и ожидание видимости элемента {wait_locator}")
    def click_and_wait_for_element(self, click_locator, wait_locator):
        self.click_element(click_locator)
        self.wait_for_element_visible(wait_locator)

    @allure.step("Подтверждение заказа")
    def confirm_order(self, order_button_locator, confirm_button_locator, status_button_locator):
        self.click_element(order_button_locator)
        self.click_element(confirm_button_locator)
        self.click_element(status_button_locator)

    @allure.step("Переход на Дзен через логотип Яндекса")
    def go_to_dzen(self, yandex_logo_locator, dzen_button_locator):
        self.click_element(yandex_logo_locator)
        self.driver.close()
        self.driver.switch_to.window()
        self.wait_for_element_clickable(dzen_button_locator)
