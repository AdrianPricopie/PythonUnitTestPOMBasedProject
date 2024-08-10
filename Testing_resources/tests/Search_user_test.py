import unittest
from selenium import webdriver
from Testing_resources.pages.main_page import MainPage as MP
from Testing_resources.Utils.UtilsDataForTests import DataTest
from Testing_resources.Utils.Environment import Environment as env
from selenium.webdriver.chrome.options import Options
from Testing_resources.pages.Product_list_page import ProductsListPage as PLP


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

        self.env = env(self.driver)

        self.PLP = PLP(self.driver)

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()

    def test_search_product(self):
        self.PLP.Enter_product(DataTest.product_name)
        self.PLP.Press_enter()
        self.PLP.Verify_the_search_results(expected_text=DataTest.product_name,
                                           test_name='test_search_product'
                                           )

    def test_search_product_that_is_not_exist(self):
        self.PLP.Enter_product(DataTest.inexisting_product)
        self.PLP.Press_enter()
        self.PLP.Verify_count_result_search_term(expected_text=DataTest.expected_result_message_for_inexisting_prod,
                                                 test_name='test_search_product_that_is_not_exist'
                                                 )

    def test_auto_suggest(self):
        self.PLP.Enter_product(DataTest.short_product_name)
        self.PLP.Verify_sugesstions(expected_result=DataTest.auto_suggest_keyword, test_name="test_auto_suggest")

    def test_search_with_numeric_input(self):
        self.PLP.Enter_product(DataTest.numeric_product_name)
        self.PLP.Press_enter()
        self.PLP.Verify_count_result_search_term(expected_text=DataTest.expected_result_message_for_numeric_input,
                                                 test_name='test_search_with_numeric_input'
                                                 )

    def test_search_with_leading_and_trailing_spaces(self):
        self.PLP.Enter_product(F"   {DataTest.product_name} ")
        self.PLP.Press_enter()
        self.PLP.Verify_the_search_results(
            expected_text=DataTest.product_name,
            test_name='test_search_with_leading_and_trailing_spaces'
        )
