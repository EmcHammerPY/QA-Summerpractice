from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException





word = "QA"



driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10) # seconds
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

driver.find_element_by_id("searchInput").send_keys(word)

driver.find_element_by_id("searchButton").click()




for index in range(1,6):
    path = f"//div[@id ='mw-content-text']//div[@class =['mw-parser-output']//ul/li[{index}]"
    print(driver.find_element_by_xpath(path).text)
    assert word in driver.find_element_by_xpath(path).text

