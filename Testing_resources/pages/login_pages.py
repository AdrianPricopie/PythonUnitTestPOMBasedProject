from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Testing_resources.Locators.Login_pages_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, user_email):
        email = self.driver.find_element(*LoginLocators.EMAIL_SELECTOR)
        email.send_keys(user_email)

    def SetPassword(self, user_password):
        password = self.driver.find_element(*LoginLocators.PASSWORD_SELECTOR)
        password.send_keys(user_password)

    def ClickSubmitButton(self):
        click_button = self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        click_button.click()

    def Get_error_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE_FOR_AUTHENTIFICATION)).text

    def Get_account_side_menu_bar(self):
        menu_list_item = self.driver.find_elements(*LoginLocators.ACCOUNT_SIDE_MENU_BAR)
        element_actual_text = []
        for element in menu_list_item:
            element_actual_text.append(element.text)
        return element_actual_text

    def ClickLogoutButton(self):
        menu_list_item = self.driver.find_elements(*LoginLocators.ACCOUNT_SIDE_MENU_BAR)
        menu_list_item[-1].click()

    def accept_cookies(self):
        self.driver.find_element(*LoginLocators.COOKIE_ACCEPT_BUTTON).click()

    def get_logout_succesfully_message(self):
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(LoginLocators.LOGOUT_SUCCES_MESSAGE,'Te-ai deconectat cu succes'))
        message_text = self.driver.find_element(*LoginLocators.LOGOUT_SUCCES_MESSAGE).text
        return message_text

    def get_validation_message_for_email_field(self):
        return self.driver.find_element(*LoginLocators.EMAIL_SELECTOR).get_attribute('validationMessage')

