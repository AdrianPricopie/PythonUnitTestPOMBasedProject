import time
from datetime import datetime

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Testing_resources.Locators.Product_list_page_locators import ProductListLocators
from assertpy import assert_that
from Testing_resources.Utils.Environment import Environment as env


class ProductsListPage:

    def __init__(self, driver):
        self.driver = driver
        errors = [NoSuchElementException, ElementNotInteractableException]
        self.wait = WebDriverWait(self.driver, timeout=15, poll_frequency=.4, ignored_exceptions=errors)
        self.env = env(self.driver)

    #
    def get_result_search_term_text_for_no_result(self):
        # Așteaptă până când textul este prezent în elementul pentru numărul de produse
        self.wait.until(
            EC.text_to_be_present_in_element(ProductListLocators.RESULT_MESSAGE_FOR_COUNT_TERM, "0 produse"))
        count_product = self.driver.find_element(*ProductListLocators.RESULT_MESSAGE_FOR_COUNT_TERM).text
        search_product = self.driver.find_element(*ProductListLocators.RESULT_MESSAGE_FOR_TERM).text
        combine_text = search_product + " " + count_product
        print(combine_text)
        return combine_text

    def Verify_count_result_search_term(self, expected_text, test_name):
        actual_result = self.get_result_search_term_text_for_no_result()
        expected_result = expected_text
        try:
            assert_that(actual_result).described_as(
                f"the {actual_result} doesn't correspond to the expected result").is_equal_to(expected_result)

        except AssertionError as e:
            self.env.take_screenshot(
                f'{test_name}_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")

            raise e

    def get_product_title_text(self, product):
        self.wait.until(
            EC.text_to_be_present_in_element(ProductListLocators.RESULT_MESSAGE_FOR_TERM,
                                             f"Rezultate pentru {product}"))

        title_products = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(ProductListLocators.PRODUCTS_ITEM_TITLE))

        return title_products[0].text

    def get_suggestions(self):
        text = self.driver.find_element(*ProductListLocators.SEARCH_SUGGESTIONS).text
        suggestions_text = text.replace("Sugestii de cautare\n", "")
        suggestions = suggestions_text.split('\n')
        return suggestions

    def Verify_sugesstions(self, expected_result, test_name):
        actual_suggest_result = self.get_suggestions()
        try:
            contains_keyword = any(
                expected_result.lower() in product.lower() for product in actual_suggest_result)

            assert_that(contains_keyword).described_as(
                f"None of the search results contain the expected text '{expected_result}'. Actual results: {actual_suggest_result}"
            ).is_true()

        except AssertionError as e:
            self.env.take_screenshot(f'{test_name}' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def get_product_title(self, product):
        possible_messages = [
            f"Rezultate pentru {product}",
            f"Produse {product}",
            f"{product}",
        ]
        message_found = False

        for msg in possible_messages:
            try:
                self.wait.until(
                    EC.text_to_be_present_in_element(ProductListLocators.RESULT_MESSAGE_FOR_TERM,
                                                     msg))
                message_found = True
                break
            except:
                continue

        if not message_found:
            raise Exception("Niciun mesaj de rezultat așteptat nu a fost găsit.")

        ele_title_products = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(ProductListLocators.PRODUCTS_ITEM_TITLE))

        title_products = []

        for ele in ele_title_products:
            title_products.append(ele.text)

        print(title_products)
        return title_products

    def Verify_the_search_results(self, expected_text, test_name):
        actual_result = self.get_product_title(expected_text)
        try:
            found = any(expected_text.lower() in title.lower() for title in actual_result)
            assert_that(found).described_as(
                f"None of the search results contain the expected text '{expected_text}'. Actual results: {actual_result}"
            ).is_true()
        except AssertionError as e:
            self.env.take_screenshot(
                f'{test_name}_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
            raise e

    def Enter_product(self, product):
        self.driver.find_element(*ProductListLocators.SEARCH_BAR).send_keys(product)

    def Press_enter(self):
        self.driver.find_element(*ProductListLocators.SEARCH_BAR).send_keys(Keys.ENTER)

    def get_prices(self):

        WebElements = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(ProductListLocators.PRODUCTS_PRICE)
        )
        prices = []

        for ele in WebElements:

            if float(ele.text.replace("Lei", "").strip()) < 1.000:

                Modify_text = ele.text.replace("Lei", "").strip()

                convert_text = float(Modify_text[:-2] + '.' + Modify_text[-2:])

                prices.append(convert_text)

            elif float(ele.text.replace("Lei", "").strip()) > 1.000:

                Modify_text = ele.text.replace("Lei", "").replace(".", "").strip()

                convert_text = float(Modify_text[:-2] + '.' + Modify_text[-2:])

                prices.append(convert_text)

        print(prices)
        return prices

    def verify_descending_price(self):
        prices = self.get_prices()

        assert len(prices) > 0, "Lista de prețuri este goală."

        for i in range(len(prices) - 1):
            try:
                assert prices[i] >= prices[
                    i + 1], f"Lista nu este ordonată descrescator la indexul {i}. Elementul {prices[i]} este mai mic decat {prices[i + 1]}."
            except AssertionError as e:
                env.take_screenshot(
                    'Test_for_descending_price_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
                raise e

    def set_price_filter(self, sort):
        time.sleep(3)
        self.driver.find_element(*ProductListLocators.SORT_BUTTON).click()

        if sort == 'Ascending'.lower() or sort == 'Ascending'.capitalize() or sort == 'Ascending':
            sort_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProductListLocators.ASSCENDING_SORT_BUTTON)
            )
            sort_button.click()
        elif sort == 'Descending'.lower():
            sort_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProductListLocators.DESCENDEING_SORT_BUTTON)
            )
            sort_button.click()

        elif sort == 'Recommendation':
            sort_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProductListLocators.RECOMMENDATION_BUTTON)
            )
            sort_button.click()

        else:
            raise ValueError(
                f"Sortare necunoscută: {sort}. Valori permise: 'Asscending', 'Descending', 'Recommendation'.")

    def verify_ascending_price(self):
        prices = self.get_prices()
        
        assert len(prices) > 0, "Lista de prețuri este goală."

        for i in range(len(prices) - 1):
            try:
                assert prices[i] <= prices[
                    i + 1], f"Lista nu este ordonată crescător la indexul {i}. Elementul {prices[i]} este mai mare decât {prices[i + 1]}."
            except AssertionError as e:
                self.env.take_screenshot(
                    'Test_for_ascending_price_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
                raise e

    def set_brand_filter(self, brand_name):
        brands_name = self.driver.find_elements(*ProductListLocators.BRANDS_NAME_BUTTON)
        for ele in brands_name:
            if ele.get_attribute('id') == brand_name.lower():
                ele.click()
                break


    def set_category_filter(self,category):
        category_name = self.driver.find_elements(*ProductListLocators.CATEGORIES)
        for ele in category_name:
            if ele.get_attribute('data-cy').split("-")[1] == category:
                ele.click()
                break
