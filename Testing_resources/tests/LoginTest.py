import time
import unittest
from datetime import datetime
from selenium import webdriver
from Testing_resources.pages.login_pages import LoginPage as LP
from Testing_resources.Utils.UtilsDataForTests import DataTest
from Testing_resources.Utils.Environment import Environment as env
from Testing_resources.pages.My_account import MyAccount_page as My_account_page
from selenium.webdriver.chrome.options import Options


class TestLoginFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page

        chrome_options = Options()

        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://flip.ro/autentifica-te/')
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)
        # Creating an object for the LoginPage class, which
        # contains the necessary methods for the login page
        self.LoginPage = LP(self.driver)

        # Accepting cookies
        self.LoginPage.accept_cookies()

        # Create an object for the DataTest class,which contains the necessary test data
        self.DataTest = DataTest

        self.env = env(self.driver)

        self.My_account_page = My_account_page(self.driver)

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_login_with_wrong_credentials(self):
        self.LoginPage.SetEmail(DataTest.wrong_email)
        self.LoginPage.SetPassword(DataTest.wrong_pass)
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Această adresă de email nu este asociată unui cont existent.'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")
        except AssertionError as e:
            self.env.take_screenshot(
                'Login_with_wrong_credentials_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_without_complete_any_field(self):
        # Testing error handling when no credentials are provided
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Adresa de e-mail lipsește.'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")
        except AssertionError as e:
            self.env.take_screenshot(
                'Login_without_complete_any_field_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_with_wrong_format_email(self):
        # Testing error handling when an incorrect email format is provided
        self.LoginPage.SetEmail(DataTest.wrong_format_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        # Checking the browser's native validation message for email field
        pop_mesage = self.LoginPage.get_validation_message_for_email_field()
        expected_result = (f"Please include an '@' in the email address. '{DataTest.wrong_format_email}' is "
                           f"missing an '@'.")
        try:
            self.assertEqual(pop_mesage, expected_result, f"the {pop_mesage} doesn't correspond to the expected result")

        except AssertionError as e:
            self.env.take_screenshot(
                'Login_with_wrong_fromat_email_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_with_correct_credentials(self):
        # Test login with correct email and password credentials
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        elements_actual_text = self.LoginPage.Get_account_side_menu_bar()
        # Expected menu items after successful login
        expected_elements = DataTest.items_pressent_in_login_dashboard
        # Verifying if the expected elements are present in the menu
        try:
            for expected_element in expected_elements:
                self.assertIn(expected_element, elements_actual_text,
                              f"Elementul '{expected_element}' lipsește din meniu,{elements_actual_text}.")
        except AssertionError as e:
            self.env.take_screenshot(
                'Login_with_correct_credentials_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_with_correct_email_field_and_wrong_password(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.wrong_pass)
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola curentă nu corespunde cu cea pe care ai introdus-o.'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")
        except AssertionError as e:
            self.env.take_screenshot(
                'Login_with_correct_email_and_wrong_pass_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_with_short_password(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.short_pass)
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola trebuie sa aiba cel putin 6 caractere'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")

        except AssertionError as e:
            self.env.take_screenshot(
                'Login_with_short_pass_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_without_complete_password_field(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola lipsește.'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")
        except AssertionError as e:
            self.env.take_screenshot(
                'Login_without_complete_pass_field_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_login_and_logout(self):
        # Test login and logout
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.ClickLogoutButton()
        actual_result = self.LoginPage.get_logout_succesfully_message()
        expected_result = 'Te-ai deconectat cu succes'
        try:
            self.assertEqual(expected_result, actual_result)
        except AssertionError as e:
            self.env.take_screenshot(
                'Login_and_logout_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_session_persistence_after_refresh(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        actual_result = self.My_account_page.get_title_account_name()
        expected_result = 'TEST TEST'
        self.driver.refresh()
        try:
            self.assertEqual(expected_result, actual_result)
        except AssertionError as e:
            self.env.take_screenshot(
                'test_session_persistence_after_refresh_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e
