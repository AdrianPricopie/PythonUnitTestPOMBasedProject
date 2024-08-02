import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Testing_resources.Locators.Search_pages_locators import SearchLocators as Locators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def Enter_product(self, product):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys(product)

    def click(self):
        self.driver.find_element(*Locators.SEARCH_BAR).send_keys(Keys.ENTER)

    def get_title_message_for_inexisting_product(self):
        title = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(Locators.FILTER_MESSAGE_TITLE))
        return title.text

    def handle_price(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*Locators.PRICE_SLIDER_FILTER)
        # 200-3280
        actions.drag_and_drop_by_offset(element, -120, 0).perform()

    def get_prices_for_products(self):
        prices_web_elements = self.driver.find_elements(*Locators.PRICE_PRODUCTS_ITEM)
        get_price = []
        for element in prices_web_elements:
            try:
                pret = element.text[:-6].replace('.', '').strip()
                if pret != 'N/A':
                    pret_convertit_float = float(pret)
                    get_price.append(pret_convertit_float)
            except ValueError:
                print(f'eroare la conversia valorii {element.text}')

        # print(f'preturile sunt: {get_price}')

        # print(get_price)
        return get_price

    def accept_cookies(self):
        self.driver.find_element(*Locators.COOKIE_ACCEPT_BUTTON).click()

    ####### new

    def select_color(self, culoare):
        time.sleep(2)
        # Wait for the color filters to be present
        colors = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(Locators.COLOR_FILTRE)
        )
        # Find the correct color filter and click it
        for element in colors:
            if element.get_attribute('title') == culoare:
                element.click()
                break

    def verify_item_title_include_expected_text(self, expected):
        time.sleep(2)
        # Wait for the product titles to be visible
        WebElements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(Locators.PRODUCT_ITEM_TITLE)
        )
        # Verify that the expected text is in the product titles
        for element in WebElements:
            assert expected in element.text, f"Expected '{expected}', but got '{element.text}'"

    def click_price_radio(self, price_range):
        radio_elements = self.driver.find_elements(*Locators.PRICE_RADIO_BUTTON_FILTER)
        for element in radio_elements:
            if element.text.strip() == price_range:
                element.click()
                break

