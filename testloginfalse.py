from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

username = "Testt121"
password = "1234567890QW"
word = "Incorrect username or password entered. Please try again."

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10) # seconds
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
driver.find_element_by_id("wpName1").send_keys(username)
driver.find_element_by_id("wpPassword1").send_keys(password)
driver.find_element_by_id("wpLoginAttempt").click()
path = f"//div[@class = 'errorbox']"
element = driver.find_element_by_xpath(path)

assert word == element.text

driver.quit()
print("SUCCSES") 