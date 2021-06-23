from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except:
            print("can't get element")
            
    def get_element_by_id(self, id):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, id))
            )
            return element
        except:
            print("can't get element")

    def input_text_by_xpath(self, text, xpath):
        pass

    def input_text_by_id(self, text, id):
        self.get_element_by_id(id).send_keys(text)

    def click_element_by_xpath(self, text, xpath):
        pass

    def click_element_by_id(self, text, id):
        pass