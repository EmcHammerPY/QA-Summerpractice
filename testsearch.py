from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait

word = "QA"


driver = webdriver.Chrome("chromedriver")

driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

driver.find_element_by_id("searchInput").send_keys(word)

driver.find_element_by_id("searchButton").click()