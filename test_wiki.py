import pytest
import requests
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
    context_object=dict()
    context_object["username"] = "Testt1212"
    context_object["password"] = "1234567890QWE"
    context_object["incorectpassword"] = "1234567890QW"
    context_object["message"] = "Incorrect username or password entered. Please try again."
    return context_object

@pytest.mark.done
def test_login_success(context, browser):
    get_element_by_id(browser, "wpName1").send_keys(context["username"])
    get_element_by_id(browser, "wpPassword1").send_keys(context["password"])
    get_element_by_id(browser, "wpLoginAttempt").click()
    path = f"//div[@id='mw-head']//li/a[@title]/.."
    element = get_element_by_xpath(browser, path)

    assert context["username"] == element.text

@pytest.mark.done
def test_login_failed(context, browser):
    get_element_by_id(browser, "wpName1").send_keys(context["username"])
    get_element_by_id(browser, "wpPassword1").send_keys(context["incorectpassword"])
    get_element_by_id(browser, "wpLoginAttempt").click()
    path = f"//div[@class = 'errorbox']"
    element = get_element_by_xpath(browser, path)

    assert context["message"] == element.text

@pytest.mark.done
@pytest.mark.search
@pytest.mark.parametrize('word', ["QA", "auto", "Python"] )
def test_search(word, browser):
    get_element_by_id(browser, "searchInput").send_keys(word)
    get_element_by_id(browser, "searchButton").click()
    path = f"//div[@id='mw-content-text']//li/a[@title]/.."
    get_element_by_xpath(browser, path)
    elements=browser.find_elements_by_xpath(path)
    for index in range(5):    
        assert word in elements[index].text

@pytest.mark.done
@pytest.mark.article
@pytest.mark.parametrize('country', ["Qatar", "Moldova", "Romania"] )
def test_api_article(country):
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{country}")
    assert country == response.json()['titles']['canonical']
    assert country == response.json()['title']
    assert country == response.json()['titles']['display']
    assert response.status_code == 200

@pytest.mark.done
@pytest.mark.fsearch
def test_api_fsearch():
    country = "qwety"
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{country}")
    assert "Not found." == response.json()['title']
    assert response.status_code == 404