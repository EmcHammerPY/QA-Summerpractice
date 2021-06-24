from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_elements_by_xpath(self, xpath):
        self.get_element_by_xpath(xpath)
        return self.driver.find_elements_by_xpath(xpath)            

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
        self.get_element_by_xpath(xpath).click()

    def click_element_by_id(self, id):
        self.get_element_by_id(id).click()

    def check_element_text_by_xpath(self, text, xpath):
        element = self.get_element_by_xpath(xpath)
        assert text == element.text

    def check_elements_by_xpath(self, text, xpath):
        elements = self.get_elements_by_xpath(xpath)
        for index in range(5):
            assert text in elements[index].text