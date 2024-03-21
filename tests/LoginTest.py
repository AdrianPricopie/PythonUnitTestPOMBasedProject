import time
import unittest
from datetime import datetime
from selenium import webdriver
from pages.login_pages import LoginPage as LP
from Locators.Login_pages_locators import LoginLocators as Selector
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLoginFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page

        self.driver = webdriver.Chrome()
        self.driver.get('https://flip.ro/autentifica-te/')
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)
        # Creating an object for the LoginPage class, which
        # contains the necessary methods for the login page
        self.LoginPage = LP(self.driver)

        # Accepting cookies
        self.LoginPage.accept_cookies()

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_login_with_wrong_credentials(self):
        self.LoginPage.SetEmail('Grigore@yahoo.com')
        self.LoginPage.SetPassword('Test123@')
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Această adresă de email nu este asociată unui cont existent.'
        self.assertEqual(actual_result, expected_result,
                         f"the {actual_result} doesn't correspond to the expected result")

    def test_login_without_complete_any_field(self):
        # Testing error handling when no credentials are provided
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Adresa de e-mail lipsește.'
        self.assertEqual(actual_result, expected_result,
                         f"the {actual_result} doesn't correspond to the expected result")

    def test_login_with_wrong_format_email(self):
        # Testing error handling when an incorrect email format is provided
        address_email = 'Test123zyahoo.com'
        self.LoginPage.SetEmail(address_email)
        self.LoginPage.SetPassword('Test123')
        self.LoginPage.ClickSubmitButton()
        # Checking the browser's native validation message for email field
        pop_mesage = self.driver.find_element(*Selector.EMAIL_SELECTOR).get_attribute('validationMessage')
        expected_result = f"Please include an '@' in the email address. '{address_email}' is missing an '@'."
        self.assertEqual(pop_mesage, expected_result, f"the {pop_mesage} doesn't correspond to the expected result")

    def test_login_with_correct_credentials(self):
        # Test login with correct email and password credentials

        self.LoginPage.SetEmail("Test123z@yahoo.com")
        self.LoginPage.SetPassword('Test123')
        self.LoginPage.ClickSubmitButton()
        elements_actual_text = self.LoginPage.Get_account_side_menu_bar()
        # Expected menu items after successful login
        expected_elements = ['Cumparaturile mele', 'Vanzarile mele', 'Garantiile mele', 'Asigurarile mele', 'Retur',
                             'Setari cont', 'Logout']
        # Verifying if the expected elements are present in the menu
        for expected_element in expected_elements:
            self.assertIn(expected_element, elements_actual_text,
                          f"Elementul '{expected_element}' lipsește din meniu,{elements_actual_text}.")

    def test_login_with_correct_login_field_and_wrong_password(self):
        self.LoginPage = LP(self.driver)
        self.LoginPage.SetEmail("Test123z@yahoo.com")
        self.LoginPage.SetPassword('Testcdsad2@')
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola curentă nu corespunde cu cea pe care ai introdus-o.'
        self.assertEqual(actual_result, expected_result,
                         f"the {actual_result} doesn't correspond to the expected result")

    def test_login_with_short_password(self):
        self.LoginPage.SetEmail("Test123z@yahoo.com")
        self.LoginPage.SetPassword('Testc')
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola trebuie sa aiba cel putin 6 caractere'
        self.assertEqual(actual_result, expected_result,
                         f"the {actual_result} doesn't correspond to the expected result")

    def test_login_without_complete_password_field(self):
        self.LoginPage.SetEmail('Bobita123@yahoo.com')
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola lipsește.'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")
        except AssertionError:
            # Capture and save screenshot in case of failure
            screenshot_name = 'C:/Users/adi_d/PycharmProjects/ProiectUnitTestExamen/screenshots/' + 'Error_message_for_login' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'

            self.driver.get_screenshot_as_file(screenshot_name)

            # Raise AssertionError without traceback information
            raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')

    def test_login_and_logout(self):
        # Test login and logout
        self.LoginPage.SetEmail("Test123z@yahoo.com")
        self.LoginPage.SetPassword('Test123')
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.ClickLogoutButton()
        time.sleep(2)
        success_message = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(Selector.LOGOUT_SUCCES_MESSAGE)
        )
        actual_result = success_message.text
        expected_result = 'Te-ai deconectat cu succes'
        assert actual_result == expected_result, (f'The actual result "{actual_result}" does not match the expected '
                                                  f'result')
