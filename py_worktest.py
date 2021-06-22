import pytest
from resources import get_element_by_id
from resources import get_element_by_xpath
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
    yield driver
    driver.quit() 

@pytest.fixture(scope="session")
def context():
    username = "Testt1212"
    password = "1234567890QWE"
    return username, password

@pytest.fixture(scope="session")
def test():
    username1 = "Testt121"
    password1 = "1234567890QW"
    word1 = "Incorrect username or password entered. Please try again."
    return username1, password1, word1

@pytest.fixture(scope="session")
def search():
    word = "QA"
    return word  

@pytest.mark.done
def test_guest_should_see_login_link(context, browser):
    username, password = context
    get_element_by_id(browser, "wpName1").send_keys(username)
    get_element_by_id(browser, "wpPassword1").send_keys(password)
    get_element_by_id(browser, "wpLoginAttempt").click()
    path = f"//div[@id='mw-head']//li/a[@title]/.."
    element = get_element_by_xpath(browser, path)

    assert username == element.text

@pytest.mark.done
def test_guest_should_see_pass_link(test, browser):
    username1, password1, word1 = test
    get_element_by_id(browser, "wpName1").send_keys(username1)
    get_element_by_id(browser, "wpPassword1").send_keys(password1)
    get_element_by_id(browser, "wpLoginAttempt").click()
    path = f"//div[@class = 'errorbox']"
    element = get_element_by_xpath(browser, path)

    assert word1 == element.text

@pytest.mark.done
def test_guest_should_see_search_link(search, browser):
    word = search
    get_element_by_id(browser, "searchInput").send_keys(word)
    get_element_by_id(browser, "searchButton").click()
    path = f"//div[@id='mw-content-text']//li/a[@title]/.."
    get_element_by_xpath(browser, path)
    elements=browser.find_elements_by_xpath(path)
    for index in range(5):    
        assert word in elements[index].text