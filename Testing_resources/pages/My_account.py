from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Testing_resources.Locators.My_account_locators import MyAccount as Locators


class MyAccount_page:

    def __init__(self, driver):
        self.driver = driver

    def get_title_account_name(self):
        title = self.driver.find_element(*Locators.ACCOUNT_NAME).text
        return title
