from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait


username = "Testt1212"
password = "1234567890QWE"


driver = webdriver.Chrome("chromedriver")
# перейти на страницу входа в github
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

# найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
driver.find_element_by_id("wpName1").send_keys(username)

# найти поле ввода пароля и также вставить пароль
driver.find_element_by_id("wpPassword1").send_keys(password)

# нажмите кнопку входа в систему
driver.find_element_by_id("wpLoginAttempt").click()
# ждем завершения состояния готовности
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password entered. Please try again."

# получаем ошибки (если есть)
errors = driver.find_elements_by_class_name("new")

# при необходимости распечатать ошибки
# для e в ошибках:
#     print(e.text)
# если мы находим это сообщение об ошибке в составе error, значит вход не выполнен
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

