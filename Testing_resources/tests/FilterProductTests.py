import unittest
from selenium import webdriver
from Testing_resources.pages.login_pages import LoginPage as LP
from Testing_resources.Utils.UtilsDataForTests import DataTest
from Testing_resources.Utils.Environment import Environment as env
from Testing_resources.pages.My_account import MyAccount_page as My_account_page
from selenium.webdriver.chrome.options import Options
from Testing_resources.pages.main_page import MainPage as MP
from Testing_resources.pages.Product_list_page import ProductsListPage as PLP


class TestFilterFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://flip.ro/magazin/')
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        # Creating an object for the LoginPage class, which contains the necessary methods for the login page
        self.LoginPage = LP(self.driver)

        # Creating an object for the DataTest class, which contains the necessary test data
        self.DataTest = DataTest

        # Creating an object for the Environment class to handle the environment-specific actions
        self.env = env(self.driver)

        # Creating an object for the MyAccount_page class, which handles actions on the 'My Account' page
        self.My_account_page = My_account_page(self.driver)

        # Creating an object for the MainPage class, which handles actions on the main page
        self.MP = MP(self.driver)

        # Accept cookies on the main page
        self.MP.accept_cookies()

        # Creating an object for the ProductsListPage class, which handles actions on the product list page
        self.PLP = PLP(self.driver)

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_descending_price(self):
        # Apply price filter in descending order
        self.PLP.set_price_filter('descending')

        # Verify that the products are sorted in descending order of price
        self.PLP.verify_descending_price()

    def test_ascending_price(self):
        # Apply price filter in ascending order
        self.PLP.set_price_filter('ascending')

        # Verify that the products are sorted in ascending order of price
        self.PLP.verify_ascending_price()

    def test_filter_by_brand(self):
        # Set the filter for a specific brand, e.g., "Apple"
        self.PLP.set_brand_filter('Apple')

        # Verify that all displayed products belong to the "Apple" brand
        self.PLP.Verify_the_search_results(expected_text='Apple',
                                           test_name='test_filter_by_brand')

    def test_filter_brand_and_descending_price(self):
        # Select the brand 'Samsung'
        self.PLP.set_brand_filter('samsung')

        # Set the price filter in descending order
        self.PLP.set_price_filter('descending')

        # Verify that the products are sorted in descending order of price
        self.PLP.verify_descending_price()

        # Verify that the search results contain the brand "Samsung"
        self.PLP.Verify_the_search_results(expected_text='Samsung',
                                           test_name='test_filter_brand_and_descending_price')

    def test_filter_brand_and_ascending_price(self):
        # Select the brand 'Apple'
        self.PLP.set_brand_filter('apple')

        # Set the price filter in ascending order
        self.PLP.set_price_filter('ascending')

        # Verify that the products are sorted in ascending order of price
        self.PLP.verify_ascending_price()

        # Verify that the search results contain the brand "Apple"
        self.PLP.Verify_the_search_results(expected_text='Apple',
                                           test_name='test_filter_brand_and_ascending_price')



