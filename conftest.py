import pytest
import json
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from resources.pathData import url_path, driver_path, resources_path


@fixture(scope="function")
def setup(request, user_config, initialize_driver):
    driver = initialize_driver
    driver.maximize_window()
    url = "https://" + user_config("username") + ":" + user_config("password") + "@" + str(Path(url_path))
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


@fixture(scope="function")
def initialize_driver(browser):

    # Chrome options
    opt_chrome = webdriver.ChromeOptions()
    opt_chrome.add_argument("--start-maximized")
    opt_chrome.add_argument('--no-sandbox')
    opt_chrome.add_argument("--disable-web-security")
    opt_chrome.add_argument('--disable-dev-shm-usage')
    opt_chrome.add_argument("--disable-popup-blocking")
    opt_chrome.add_argument("disable-infobars")
    opt_chrome.add_argument("--disable-extensions")
    opt_chrome.add_argument("--allow-running-insecure-content")
    opt_chrome.add_argument("--ignore-certificate-errors")
    opt_chrome.add_argument("--ignore-ssl-errors")
    # opt_chrome.add_argument("--headless")

    # Firefox options
    opt_firefox = webdriver.FirefoxOptions()
    opt_firefox.add_argument("--start-maximized")

    if browser not in ["chrome", "firefox"]:
        raise Exception(f"{browser} this browser is not supported")

    # Browser selector is based on @fixtures/addoption
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(Path(driver_path)), options=opt_chrome)
        driver.implicitly_wait(10)
        return driver
    elif browser == "firefox":
        driver = webdriver.Firefox(options=opt_firefox)
        driver.implicitly_wait(10)
        return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browsers: chrome, firefox"
    )
    parser.addoption(
        "--user",
        action="store",
        default="user_main",
        help="users: user_main"
    )


@fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    return browser


@fixture(scope='session')
def get_user(request):
    return request.config.getoption("--user")


@pytest.fixture(scope='function')
def user_config(get_user):
    def _json_param(string_of_json):
        json_input_file = Path(resources_path, 'user_parameters.json')
        with open(json_input_file) as json_data:
            json_user_data = json.load(json_data)
            i = 0
            for i in range(len(json_user_data[get_user])):
                return json_user_data[get_user][i][string_of_json]

    return _json_param
