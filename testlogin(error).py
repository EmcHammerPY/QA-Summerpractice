from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait


username = "Testt1212"
password = "1234567890QW"


driver = webdriver.Chrome("chromedriver")
# перейти на страницу входа в github
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

# найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
driver.find_element_by_id("wpName1").send_keys(username)

# найти поле ввода пароля и также вставить пароль
driver.find_element_by_id("wpPassword1").send_keys(password)

# нажмите кнопку входа в систему
driver.find_element_by_id("wpLoginAttempt").click()

