import time
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage as MP


class TestSearchFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page

        self.driver = webdriver.Chrome()
        self.driver.get('https://flip.ro/magazin/')
        self.driver.maximize_window()

        # Accepting cookies

        self.driver.find_element(By.XPATH, '//span[contains(text(), "Da, sunt de acord")]').click()
        self.driver.implicitly_wait(5)
        self.Search = MP(self.driver)

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_search_product(self):
        self.Search.Enter_product('Iphone 14')
        self.Search.click()
        actual_result = self.Search.get_product_title_text()
        expected_result = 'iPhone 14'
        time.sleep(2)
        try:
            self.assertIn(expected_result, actual_result, f"The expected result is not found in the {actual_result}.")
        except AssertionError:
            # Capture and save screenshot in case of failure
            screenshot_name = 'C:/Users/adi_d/PycharmProjects/ProiectUnitTestExamen/screenshots/' + 'Error_message_for_search_product' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'

            self.driver.get_screenshot_as_file(screenshot_name)

            # Raise AssertionError without traceback information
            raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')

    def test_search_product_that_is_not_exist(self):
        self.Search.Enter_product('fdsafdasfd')
        self.Search.click()
        actual_result = self.Search.get_title_message_for_inexisting_product()
        expected_result = 'Nu există produse pentru filtrele aplicate.'
        time.sleep(2)
        try:
            self.assertEqual(actual_result, expected_result, f"The expected result is not found in the {actual_result}.")
        except AssertionError:
            # Capture and save screenshot in case of failure
            screenshot_name = 'C:/Users/adi_d/PycharmProjects/ProiectUnitTestExamen/screenshots/' + 'Error_message_for_search_a_product_that_is_not_exist' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'

            self.driver.get_screenshot_as_file(screenshot_name)

            # Raise AssertionError without traceback information
            raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')

    def test_filter_by_price(self):
        self.Search.Enter_product('Iphone 13')
        self.Search.click()
        time.sleep(4)
        self.Search.handle_price()
        time.sleep(2)
        interval_cautare = (200, 3515)
        price = self.Search.get_prices_for_products()
        for elemente in price:
            try:
                self.assertTrue(interval_cautare[0] <= elemente <= interval_cautare[1],
                                f'Eroare: Elementul {elemente} nu se află în intervalul filtrat.')

            except AssertionError:
                # Capture and save screenshot in case of failure
                screenshot_name = 'C:/Users/adi_d/PycharmProjects/ProiectUnitTestExamen/screenshots/' + 'Error_message_for_search_product_filter_by_price' + '_' + datetime.now().strftime(
                    '%d-%m-%Y') + '.png'

                self.driver.get_screenshot_as_file(screenshot_name)

                # Raise AssertionError without traceback information
                raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')
