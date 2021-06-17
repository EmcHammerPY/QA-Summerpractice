from resources import get_element_by_id
from resources import get_element_by_xpath
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

username = "Testt1212"
password = "1234567890QWE"

driver = webdriver.Chrome("chromedriver")
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
get_element_by_id(driver, "wpName1").send_keys(username)
driver.find_element_by_id("wpPassword1").send_keys(password)
driver.find_element_by_id("wpLoginAttempt").click()
path = f"//div[@id='mw-head']//li/a[@title]/.."
elements =get_element_by_xpath(driver, path)

assert username == elements.text

driver.quit()
print("SUCCSES") 