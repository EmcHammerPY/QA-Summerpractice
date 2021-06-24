from pages.base_page import BasePage

class LoginPage(BasePage):
    username_id = "wpName1"
    password_id = "wpPassword1"
    login_button_id = "wpLoginAttempt"
    check_username_xpath = f"//div[@id='mw-head']//li/a[@title]/.."
    check_error_xpath = f"//div[@class = 'errorbox']"


    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, text):
        self.input_text_by_id(text, self.username_id)

    def input_password(self, text):
        self.input_text_by_id(text, self.password_id)

    def click_on_login_button(self):
        self.click_element_by_id(self.login_button_id)

    def check_username(self, text):
        self.check_element_text_by_xpath(text, self.check_username_xpath)

    def check_error_message(self, text):
        self.check_element_text_by_xpath(text, self.check_error_xpath)