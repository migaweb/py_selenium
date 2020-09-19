from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = webdriver.Chrome()
browser.get('http://techstepacademy.com/training-ground')


def alert(browser):
    alert = Alert(browser)
    btn = browser.find_element_by_id('b1')
    btn.click()
    alert.dismiss()


def wait(browser):
    print('I have arrived')
    WebDriverWait(browser, 10).until(alert_is_present())
    print('An alert appeared')


def select(browser):
    select_el = browser.find_element_by_id('sel1')
    my_sel = Select(select_el)
    my_sel.select_by_value('second')  # Beets


# browser.close()
