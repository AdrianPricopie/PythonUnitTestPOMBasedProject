from Testing_resources.Locators.Main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIE_ACCEPT_BUTTON).click()
