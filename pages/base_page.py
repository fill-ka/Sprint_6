import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Инициализация драйвера")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие сайта: {site}")
    def open_site(self, site):
        self.driver.get(site)

    @allure.step("Заполнение поля: {locator} сообщением: {message}")
    def fill_input(self, locator, message):
        self.driver.find_element(*locator).send_keys(message)

    @allure.step("Прокрутка до элемента: {locator}")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Клик по кнопке cookies: {locator}")
    def click_cookie_button(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Прокрутка до элемента и клик: {locator}")
    def scroll_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Переход в новое окно")
    def switch_to_new_window(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    @allure.step("Получение текущего url")
    def get_current_url(self):
        return self.driver.current_url
