
from selenium import webdriver
from pages.trial_page import TrialPage
from pages.training_ground_page import TrainingGroundPage

browser = webdriver.Chrome()
stones_answer = 'rock'

# Trial page
trial_page = TrialPage(driver=browser)
trial_page.go()

trial_page.stone_input.input_text(stones_answer)
trial_page.stone_button.click()

input()

# Training grounds
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', 'Unexpected button1 text'
print('[+] Test passed training ground page')
input()

browser.quit()
