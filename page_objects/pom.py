from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)
        return None

    def alert_dismiss(self):
        Alert(browser).dismiss()
        return None

    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('ipt1')
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        inpt = self.driver.find_element_by_id('ipt1')
        return inpt.get_attribute('value')

    def click_button_1(self):
        btn = self.driver.find_element_by_id('b1')
        btn.click()
        return None


# Test setup
test_value = 'hello world'
browser = webdriver.Chrome()

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input(test_value)
trng_page.click_button_1()
trng_page.alert_dismiss()

text_from_input = trng_page.get_input_text()
assert text_from_input == test_value, f'Test failed: Input did not match expected ({test_value}).'
print('test passed')

browser.close()
