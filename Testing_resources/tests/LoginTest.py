import unittest
from selenium import webdriver
from Testing_resources.pages.login_pages import LoginPage as LP
from Testing_resources.Utils.UtilsDataForTests import DataTest
from Testing_resources.pages.My_account import MyAccount_page as My_account_page
from selenium.webdriver.chrome.options import Options
from Testing_resources.pages.main_page import MainPage as Mp


class TestLoginFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://flip.ro/autentifica-te/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # Creating an object for the LoginPage class
        self.LoginPage = LP(self.driver)

        # Creating an object for the DataTest class, which contains the test data
        self.DataTest = DataTest

        # Creating an object for the MyAccount_page class
        self.My_account_page = My_account_page(self.driver)

        # Creating an object for the MainPage class and accepting cookies
        self.Mp = Mp(self.driver)
        self.Mp.accept_cookies()

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_login_with_wrong_credentials(self):
        self.LoginPage.SetEmail(DataTest.wrong_email)
        self.LoginPage.SetPassword(DataTest.wrong_pass)
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.Verify_toast_error_message(
            expected_message='Această adresă de email nu este asociată unui cont existent.',
            test_name='Test_login_with_wrong_cre'

        )

    def test_login_without_complete_any_field(self):
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.Verify_toast_error_message(expected_message='Adresa de e-mail lipsește.',
                                                  test_name='test_login_without_complete_any_field'
                                                  )

    def test_login_with_wrong_format_email(self):
        # Testing error handling when an incorrect email format is provided
        self.LoginPage.SetEmail(DataTest.wrong_format_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        # Checking the browser's native validation message for email field
        self.LoginPage.Verify_email_validation_message(
            expected_message=f"Please include an '@' in the email address. '{DataTest.wrong_format_email}' is "
                             f"missing an '@'.", test_name='Test_login_with_wrong_format_email')

    def test_login_with_correct_credentials(self):
        # Test login with correct email and password credentials
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        self.My_account_page.verify_elements_in_account_present(
            expected_elements=DataTest.items_pressent_in_login_dashboard,
            test_name="test_login_with_correct_cred")

    def test_login_with_correct_email_field_and_wrong_password(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.wrong_pass)
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.Verify_toast_error_message(
            expected_message='Parola curentă nu corespunde cu cea pe care ai introdus-o.',
            test_name='test_login_with_correct_email_and_wrong_pass')

    def test_login_with_short_password(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.short_pass)
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.Verify_toast_error_message(expected_message='Parola trebuie sa aiba cel putin 6 caractere', test_name='test_login_with_short_pass'
                                                  )

    def test_login_without_complete_password_field(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.Verify_toast_error_message(expected_message='Parola lipsește.',
                                                  test_name='test_login_without_complete_pass')

    def test_login_and_logout(self):
        # Test login and logout
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        self.LoginPage.ClickLogoutButton()
        self.LoginPage.Verify_succesfully_logout_message(expected_message='Te-ai deconectat cu succes',
                                                         test_name='Test_login_and_logout')

    def test_session_persistence_after_refresh(self):
        self.LoginPage.SetEmail(DataTest.correct_email)
        self.LoginPage.SetPassword(DataTest.correct_pass)
        self.LoginPage.ClickSubmitButton()
        self.My_account_page.verify_title_name_in_my_account(expected_message='TEST TEST', test_name='test_session_persistence_after_refresh')
        self.driver.refresh()
        self.My_account_page.verify_title_name_in_my_account(expected_message='TEST TEST', test_name='test_session_persistence_after_refresh')
