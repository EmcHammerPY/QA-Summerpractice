from pages.base_page import BasePage

class SearchPage(BasePage):
    search_input = "searchInput"
    search_button = "searchButton"
    check_word_xpath = f"//div[@id='mw-content-text']//li/a[@title]/.."

    def __init__(self, driver):
        super().__init__(driver)

    def input_word(self, text):
        self.input_text_by_id(text, self.search_input)

    def click_on_search_button(self):
        self.click_element_by_id(self.search_button)

    def check_word(self, text):
        self.check_elements_by_xpath(text, self.check_word_xpath)