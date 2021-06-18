from resources import get_element_by_id
from resources import get_element_by_xpath
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


word = "QA"

driver = webdriver.Chrome("chromedriver")
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
get_element_by_id(driver, "searchInput").send_keys(word)
get_element_by_id(driver, "searchButton").click()
path = f"//div[@id='mw-content-text']//li/a[@title]/.."
elements=driver.find_elements_by_xpath(path)
get_element_by_xpath(driver, path)
for index in range(5):    
    assert word in elements[index].text
driver.quit()
print("SUCCSES")