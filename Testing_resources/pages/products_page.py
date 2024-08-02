import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Testing_resources.Locators.Search_pages_locators import SearchLocators as Locators


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        errors = [NoSuchElementException, ElementNotInteractableException]
        self.wait = WebDriverWait(self.driver, timeout=15, poll_frequency=.4, ignored_exceptions=errors)

    def get_result_search_term_text(self):
        # Așteaptă până când textul este prezent în elementul pentru numărul de produse
        self.wait.until(EC.text_to_be_present_in_element(Locators.RESULT_MESSAGE_FOR_COUNT_TERM, "0 produse"))
        count_product = self.driver.find_element(*Locators.RESULT_MESSAGE_FOR_COUNT_TERM).text
        search_product = self.driver.find_element(*Locators.RESULT_MESSAGE_FOR_TERM).text
        combine_text = search_product + " " + count_product
        return combine_text

    def get_product_title_text(self, product):
        self.wait.until(
            EC.text_to_be_present_in_element(Locators.RESULT_MESSAGE_FOR_TERM, f"Rezultate pentru {product}"))

        title_products = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(Locators.PRODUCTS_ITEM_TITLE))

        return title_products[0].text

    def get_suggestions(self):
        text = self.driver.find_element(*Locators.SEARCH_SUGGESTIONS).text
        suggestions_text = text.replace("Sugestii de cautare\n", "")
        suggestions = suggestions_text.split('\n')
        return suggestions

    def get_product_title(self, product):
        self.wait.until(
            EC.text_to_be_present_in_element(Locators.RESULT_MESSAGE_FOR_TERM, f"Rezultate pentru {product}"))

        ele_title_products = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(Locators.PRODUCTS_ITEM_TITLE))

        title_products = []

        for ele in ele_title_products:
            title_products.append(ele.text)

        print(title_products)
        return title_products
