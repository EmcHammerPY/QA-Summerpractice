import pytest
import requests
import pyautogui
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")
    yield driver
   # time.sleep(1)
   # driver.get_screenshot_as_file('Wikitest.png') 
    driver.quit() 

@pytest.fixture(scope="session")
def context():
    context_object=dict()
    context_object["username"] = "Testt1212"
    context_object["word"] = "QA"
    context_object["password"] = "1234567890QWE"
    context_object["incorectpassword"] = "1234567890QW"
    context_object["message"] = "Incorrect username or password entered. Please try again."
    return context_object

@pytest.mark.done
@pytest.mark.login
def test_login_success(context, browser):
    lp = LoginPage(browser)
    lp.input_username(context["username"])
    time.sleep(1)
    lp.input_password(context["password"])
    time.sleep(1)
    lp.click_on_login_button()
    lp.check_username(context["username"])

@pytest.mark.done
@pytest.mark.false
def test_login_failed(context, browser):
    lp = LoginPage(browser)
    lp.input_username(context["username"])
    lp.input_password(context["incorectpassword"])
    lp.click_on_login_button()
    lp.check_error_message(context["message"])

@pytest.mark.done
@pytest.mark.search
@pytest.mark.parametrize('word', ["QA"] )
def test_search(word, browser):
    lp = SearchPage(browser)
    lp.input_word(word)
    lp.click_on_search_button()
    lp.check_word(word)


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