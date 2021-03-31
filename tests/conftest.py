from pytest import fixture
from selenium import webdriver


@fixture(scope='function')  # function, session, module, class
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    # Teardown code
    print('I am tearing down this browser')
