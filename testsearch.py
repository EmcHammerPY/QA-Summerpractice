from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

word = "QA"

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10) # seconds
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
driver.find_element_by_id("searchInput").send_keys(word)
driver.find_element_by_id("searchButton").click()
path = f"//div[@id='mw-content-text']//li/a[@title]/.."
elements=driver.find_elements_by_xpath(path)
for index in range(5):    
    assert word in elements[index].text
driver.quit()
print("SUCCSES")