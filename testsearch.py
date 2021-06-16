from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException




word = "QA"



driver = webdriver.Chrome("chromedriver")

driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")

driver.find_element_by_id("searchInput").send_keys(word)

driver.find_element_by_id("searchButton").click()


from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_id("content"))
select.select_by_visible_text("QA")

words = ['word', 'word1', 'word2']
site = urllib.request.urlopen(link)
for word in words:
    if word in site:
       print(word)
    else:
       print(word, "not found")