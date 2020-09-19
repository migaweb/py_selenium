from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def wait_for_ajax(driver):
    wait = WebDriverWait(driver, 15)
    try:
        wait.until(lambda driver: driver.execute_script(
            'return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script(
            'return document.readyState') == 'complete')
    except Exception:
        pass


def login(browser):
    user_el = browser.find_element_by_id('Username')
    pw_el = browser.find_element_by_id('Password')
    submit_btn = browser.find_element_by_id('btnLogin')

    user_el.send_keys('')
    pw_el.send_keys('')
    submit_btn.click()

    WebDriverWait(browser, 20).until(
        lambda x: x.find_element_by_id('BranchId'))

    browser.execute_script(
        "$('#BranchId').data('kendoDropDownList').select(1);")
    wait_for_ajax(browser)
    browser.execute_script(
        "$('#Department').data('kendoDropDownList').select(1);")

    browser.find_element_by_id('btnOk').click()


def kendo_drop_select(browser, branch_el, item_index):
    branch_el.click()


def click_on_module(browser):
    burger_a = browser.find_element_by_id(
        'ctl00__ucMenu__lvModules_ctrl4__lbToggle')
    burger_a.click()


browser = webdriver.Chrome()
browser.get('https://demo.compilator.com/login/login')

login(browser)
