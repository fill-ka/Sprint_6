from selenium.webdriver.common.keys import Keys
import time
from pages.base_page import BasePage


class OrderPage(BasePage):

    def select_scooter_color(self, locator):
        self.driver.find_element(*locator).click()

    def fill_customer_info(self, name_locator, name, surname_locator, surname, address_locator, address,
                           phone_locator, phone, metro_locator, metro):
        self.fill_input(name_locator, name)
        self.fill_input(surname_locator, surname)
        self.fill_input(address_locator, address)
        self.fill_input(phone_locator, phone)
        time.sleep(2)
        metro_input = self.driver.find_element(*metro_locator)
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    def fill_rental_info(self, rental_period_locator, period_locator, color_locator, date_locator, date, comment_locator, comment):
        self.fill_input(date_locator, date)
        self.driver.find_element(*date_locator).send_keys(Keys.ENTER)
        self.click_element(rental_period_locator)
        self.click_element(period_locator)
        self.click_element(color_locator)
        self.fill_input(comment_locator, comment)

    def wait_and_click(self, locator):
        self.wait_for_element_clickable(locator)
        self.click_element(locator)

    def click_and_wait_for_element(self, click_locator, wait_locator):
        self.click_element(click_locator)
        self.wait_for_element_visible(wait_locator)

    def confirm_order(self, order_button_locator, confirm_button_locator, status_button_locator):
        self.click_element(order_button_locator)
        self.click_element(confirm_button_locator)
        self.click_element(status_button_locator)

    def go_to_dzen(self, yandex_logo_locator, dzen_button_locator):
        self.click_element(yandex_logo_locator)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.wait_for_element_clickable(dzen_button_locator)
