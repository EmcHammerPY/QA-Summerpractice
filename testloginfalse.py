from resources import get_element_by_id
from resources import get_element_by_xpath
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

username = "Testt121"
password = "1234567890QW"
word = "Incorrect username or password entered. Please try again."

driver = webdriver.Chrome("chromedriver")
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
get_element_by_id(driver, "wpName1").send_keys(username)
get_element_by_id(driver, "wpPassword1").send_keys(password)
get_element_by_id(driver, "wpLoginAttempt").click()
path = f"//div[@class = 'errorbox']"
element=get_element_by_xpath(driver, path)

assert word == element.text

driver.quit()
print("SUCCSES") 