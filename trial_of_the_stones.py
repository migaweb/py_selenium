from selenium import webdriver


def create_browser(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser


def riddle_of_stone(browser):
    input_element = browser.find_element_by_id('r1Input')
    btn_element = browser.find_element_by_css_selector('button[id="r1Btn"]')
    input_element.send_keys('rock')
    btn_element.click()
    answer_element = browser.find_element_by_css_selector(
        'div[id="passwordBanner"] > h4')

    return answer_element.text


def riddle_of_secrets(browser, password):
    input_element = browser.find_element_by_css_selector('input[id="r2Input"]')
    input_element.send_keys(password)
    btn_element = browser.find_element_by_css_selector('button[id="r2Butn"]')
    btn_element.click()


def richest_merchant(browser):
    input_element = browser.find_element_by_css_selector('input[id="r3Input"]')
    input_element.send_keys('Jessica')
    btn_element = browser.find_element_by_css_selector('button[id="r3Butn"]')
    btn_element.click()


def richest_merchant_2(browser):
    richest_merchant_name = browser.find_element_by_xpath(
        "//p[text()='3000']/../span")
    input_element = browser.find_element_by_css_selector('input[id="r3Input"]')
    input_element.send_keys(richest_merchant_name.text)
    btn_element = browser.find_element_by_css_selector('button[id="r3Butn"]')
    btn_element.click()


def check_answer(browser):
    btn_element = browser.find_element_by_css_selector(
        'button[id="checkButn"]')
    btn_element.click()
    complete_element = browser.find_element_by_css_selector(
        'div#trialCompleteBanner >h4')
    assert complete_element.text == 'Trial Complete'


browser = create_browser('https://techstepacademy.com/trial-of-the-stones')
riddle_of_stone_answer = riddle_of_stone(browser)
riddle_of_secrets(browser, riddle_of_stone_answer)
richest_merchant_2(browser)
check_answer(browser)
browser.close()
