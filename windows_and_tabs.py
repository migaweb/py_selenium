from selenium import webdriver


def open_tab(browser, url):
    browser.execute_script("window.open('{url}', '_blank');")


browser = webdriver.Chrome()
browser.get('http://techstepacademy.com/training_ground')
open_tab(browser, 'http://www.google.com')
open_tab(browser, 'http://www.google.com')

handles = browser.window_handles
print(handles)
print(len(handles))

browser.switch_to.window(handles[2])
# browser.close()
