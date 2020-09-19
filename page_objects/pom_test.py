from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage


# Test setup
test_value = 'hello world'
browser = webdriver.Chrome()

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', f'Test failed'
print('Test passed')
trng_page.button1.click()
trng_page.alert_dismiss()

browser.close()
