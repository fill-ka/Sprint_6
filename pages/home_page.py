from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class HomePage(BasePage):

    def search_question_and_open_answer(self, question, answer):
        element_scroll = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_scroll)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(answer))
        text = self.driver.find_element(*answer).text
        return text