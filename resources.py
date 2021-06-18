from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_element_by_xpath(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except:
        print("can't get element")

        
def get_element_by_id(driver, id):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, id))
        )
        return element
    except:
        print("can't get element")

