from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Testing_resources.Locators.Login_pages_locators import LoginLocators
from Testing_resources.Locators.My_account_locators import MyAccountLocators
from assertpy import assert_that
from Testing_resources.Utils.Environment import Environment as env


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.env = env(self.driver)

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
            EC.visibility_of_element_located(LoginLocators.TOAST_MESSAGE_ERROR_FOR_AUTHENTIFICATION)).text

    def Verify_toast_error_message(self, expected_message, test_name):
        actual_result = self.Get_error_message()
        expected_result = expected_message
        try:
            assert_that(actual_result).described_as(
                f"the {actual_result} doesn't correspond to the expected result").is_equal_to(expected_result)
        except AssertionError as e:
            self.env.take_screenshot(
                f'{test_name}_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")

            raise e

    def ClickLogoutButton(self):
        menu_list_item = self.driver.find_elements(*MyAccountLocators.ACCOUNT_SIDE_MENU_BAR)
        menu_list_item[-1].click()

    def get_logout_succesfully_message(self):
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(LoginLocators.TOAST_MESSAGE_FOR_SUCCES_LOGOUT,
                                             'Te-ai deconectat cu succes'))
        message_text = self.driver.find_element(*LoginLocators.TOAST_MESSAGE_FOR_SUCCES_LOGOUT).text
        return message_text

    def Verify_succesfully_logout_message(self, expected_message, test_name):
        actual_result = self.get_logout_succesfully_message()
        expected_result = expected_message
        try:
            assert_that(actual_result).described_as(
                f"the {actual_result} doesn't correspond to the expected result").is_equal_to(expected_result)

        except AssertionError as e:
            self.env.take_screenshot(
                f'{test_name}_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")

            raise e

    def get_validation_message_for_email_field(self):
        return self.driver.find_element(*LoginLocators.EMAIL_SELECTOR).get_attribute('validationMessage')

    def Verify_email_validation_message(self, expected_message, test_name):
        actual_result = self.get_validation_message_for_email_field()
        expected_result = expected_message
        try:
            assert_that(actual_result).described_as(
                f"the {actual_result} doesn't correspond to the expected result").is_equal_to(expected_result)

        except AssertionError as e:
            self.env.take_screenshot(
                f'{test_name}_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")

            raise e
