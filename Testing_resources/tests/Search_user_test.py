import unittest
from datetime import datetime
from selenium import webdriver
from Testing_resources.pages.main_page import MainPage as MP
from Testing_resources.Utils.UtilsDataForTests import DataTest
from Testing_resources.pages.products_page import ProductsPage
from Testing_resources.Utils.Environment import Environment as env
from selenium.webdriver.chrome.options import Options


class TestSearchFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page
   
        chrome_options = Options()

        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get('https://flip.ro/magazin/')

        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.Search = MP(self.driver)

        # Accepting cookies
        self.Search.accept_cookies()

        # Create an object for the DataTest class,which contains the necessary test data
        self.DataTest = DataTest

        self.ProductsPage = ProductsPage(self.driver)

        self.env = env(self.driver)

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_search_product(self):
        self.Search.Enter_product(DataTest.product_name)
        self.Search.click()

        actual_result = self.ProductsPage.get_product_title_text(DataTest.product_name)
        expected_result = DataTest.product_name

        try:
            self.assertIn(expected_result, actual_result, f"The expected result is not found in the {actual_result}.")
        except AssertionError as e:
            self.env.take_screenshot('test_search_product_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_search_product_that_is_not_exist(self):
        self.Search.Enter_product(DataTest.inexisting_product)
        self.Search.click()
        actual_result = self.ProductsPage.get_result_search_term_text()
        expected_result = f'Rezultate pentru {DataTest.inexisting_product} 0 produse'
        try:
            self.assertEqual(actual_result, expected_result, f"The expected result is not in the {actual_result}")
        except AssertionError as e:
            self.env.take_screenshot(
                'search_product_that_is_not_exist_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_auto_suggest(self):
        self.Search.Enter_product(DataTest.short_product_name)
        try:
            actual_suggest_result = self.ProductsPage.get_suggestions()

            contains_keyword = any(
                DataTest.auto_suggest_keyword.lower() in product.lower() for product in actual_suggest_result)

            self.assertTrue(contains_keyword,
                            f"None of the products contain the keyword 'iPhone': {actual_suggest_result}")
        except AssertionError as e:
            self.env.take_screenshot('test_auto_suggest' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_search_with_numeric_input(self):
        self.Search.Enter_product(DataTest.numeric_product_name)
        self.Search.click()

        try:
            actual_result = self.ProductsPage.get_result_search_term_text()
            expected_result = f'Rezultate pentru {DataTest.numeric_product_name} 0 produse'
            self.assertEqual(actual_result, expected_result, f"The expected result is not in the {actual_result}")
        except AssertionError as e:
            self.env.take_screenshot(
                'test_search_with_numeric_input_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def test_search_with_special_characters_various_positions(self):
        self.Search.Enter_product(DataTest.special_product_name)
        self.Search.click()

        try:
            actual_result = self.ProductsPage.get_product_title(DataTest.special_product_name)
            contains_keyword = any(
                any(keyword.lower() in product_title.lower() for keyword in DataTest.expected_result_search) for
                product_title in
                actual_result)
            self.assertTrue(contains_keyword,
                            f"None of the expected keywords found in the product title: {actual_result}")

        except AssertionError as e:
            self.env.take_screenshot(
                'test_search_with_special_characters_various_positions_failure' + '_' + datetime.now().strftime(
                    '%d-%m-%Y') + "_")
            raise e
