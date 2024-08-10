import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class Environment:

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, name):
        screenshots_dir = 'screenshots'
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        self.driver.save_screenshot(os.path.join(screenshots_dir, f'{name}.png'))
