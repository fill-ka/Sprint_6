from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_site(self, site):
        self.driver.get(site)

    def fill_input(self, locator, message):
        self.driver.find_element(*locator).send_keys(message)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def click_cookie_button(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(locator))

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_element_clickable(locator)
        element.click()
