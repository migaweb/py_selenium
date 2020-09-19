
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from .base_element import BaseElement


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)
        return None

    def alert_dismiss(self):
        Alert(self.driver).dismiss()
        return None

    @property
    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
