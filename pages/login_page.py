from base_page import BasePage

class LoginPage(BasePage):
    username_id = "wpName1"
    password_id = "wpPassword1"
    login_button = "wpLoginAttempt"
    check_username_xpath = "//div[@id='mw-head']//li/a[@title]/.."

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, text):
        self.input_text_by_id(text, self.username_id)

    def input_password(self, text):
        pass

    def click_on_login_button(self):
        pass

    def check_username(self):
        pass