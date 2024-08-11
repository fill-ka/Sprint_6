import allure
from pages.base_page import BasePage

class HomePage(BasePage):

    @allure.step("Поиск вопроса и открытие ответа")
    def search_question_and_open_answer(self, question, answer):
        self.scroll_to_element(question)
        self.wait_for_element_clickable(question)
        self.click_element(question)
        self.wait_for_element_visible(answer)
        return self.get_element_text(answer)
