
from selenium import webdriver

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"
product1_locator = '//b[text()="Product 1"]/../../p'

browser = webdriver.Chrome()
browser.get('https:\\techstepacademy.com/training-ground')

# assign elements
input2_elem = browser.find_element_by_css_selector(input2_css_locator)
butn4_elem = browser.find_element_by_xpath(button4_xpath_locator)

# Manipulate elements
input2_elem.send_keys('hello world')
butn4_elem.click()

# browser.quit()
