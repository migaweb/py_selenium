from selenium.webdriver.common.alert import Alert


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
        return None

    def alert_dismiss(self):
        Alert(self.driver).dismiss()
        return None
