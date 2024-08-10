from Testing_resources.Locators.Main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    #
    #
    # def click(self):
    #     self.driver.find_element(*SearchLocators.SEARCH_BAR).send_keys(Keys.ENTER)
    #
    # def get_title_message_for_inexisting_product(self):
    #     title = WebDriverWait(self.driver, 15).until(
    #         EC.visibility_of_element_located(SearchLocators.FILTER_MESSAGE_TITLE))
    #     return title.text
    #
    # def handle_price(self):
    #     actions = ActionChains(self.driver)
    #     element = self.driver.find_element(*SearchLocators.PRICE_SLIDER_FILTER)
    #     # 200-3280
    #     actions.drag_and_drop_by_offset(element, -120, 0).perform()
    #
    # def get_prices_for_products(self):
    #     prices_web_elements = self.driver.find_elements(*SearchLocators.PRICE_PRODUCTS_ITEM)
    #     get_price = []
    #     for element in prices_web_elements:
    #         try:
    #             pret = element.text[:-6].replace('.', '').strip()
    #             if pret != 'N/A':
    #                 pret_convertit_float = float(pret)
    #                 get_price.append(pret_convertit_float)
    #         except ValueError:
    #             print(f'eroare la conversia valorii {element.text}')
    #
    #     # print(f'preturile sunt: {get_price}')
    #
    #     # print(get_price)
    #     return get_price
    #
    #
    # ####### new
    #
    # def select_color(self, culoare):
    #     time.sleep(2)
    #     # Wait for the color filters to be present
    #     colors = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_all_elements_located(SearchLocators.COLOR_FILTRE)
    #     )
    #     # Find the correct color filter and click it
    #     for element in colors:
    #         if element.get_attribute('title') == culoare:
    #             element.click()
    #             break
    #
    # def verify_item_title_include_expected_text(self, expected):
    #     time.sleep(2)
    #     # Wait for the product titles to be visible
    #     WebElements = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_all_elements_located(SearchLocators.PRODUCT_ITEM_TITLE)
    #     )
    #     # Verify that the expected text is in the product titles
    #     for element in WebElements:
    #         assert expected in element.text, f"Expected '{expected}', but got '{element.text}'"
    #
    # def click_price_radio(self, price_range):
    #     radio_elements = self.driver.find_elements(*SearchLocators.PRICE_RADIO_BUTTON_FILTER)
    #     for element in radio_elements:
    #         if element.text.strip() == price_range:
    #             element.click()
    #             break
    #
    # def set_price_filter(self, sort):
    #     time.sleep(2)
    #     self.driver.find_element(*MyAccountLocators.SORT_BUTTON).click()
    #
    #     if sort == 'Ascending'.lower() or sort == 'Ascending'.capitalize() or sort == 'Ascending':
    #         sort_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(MyAccountLocators.ASSCENDING_SORT_BUTTON)
    #         )
    #         sort_button.click()
    #     elif sort == 'Descending'.lower():
    #         sort_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(MyAccountLocators.DESCENDEING_SORT_BUTTON)
    #         )
    #         sort_button.click()
    #
    #     elif sort == 'Recommendation':
    #         sort_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(MyAccountLocators.RECOMMENDATION_BUTTON)
    #         )
    #         sort_button.click()
    #
    #     else:
    #         raise ValueError(
    #             f"Sortare necunoscută: {sort}. Valori permise: 'Asscending', 'Descending', 'Recommendation'.")
    #
    # def get_prices(self):
    #
    #     WebElements = WebDriverWait(self.driver, 15).until(
    #         EC.presence_of_all_elements_located(MyAccountLocators.PRODUCTS_PRICE)
    #     )
    #     prices = []
    #
    #     for ele in WebElements:
    #
    #         if float(ele.text.replace("Lei", "").strip()) < 1.000:
    #
    #             Modify_text = ele.text.replace("Lei", "").strip()
    #
    #             convert_text = float(Modify_text[:-2] + '.' + Modify_text[-2:])
    #
    #             prices.append(convert_text)
    #
    #         elif float(ele.text.replace("Lei", "").strip()) > 1.000:
    #
    #             Modify_text = ele.text.replace("Lei", "").replace(".", "").strip()
    #
    #             convert_text = float(Modify_text[:-2] + '.' + Modify_text[-2:])
    #
    #             prices.append(convert_text)
    #
    #     print(prices)
    #     return prices
    #
    # def verify_ascendeing_price(self):
    #     prices = self.get_prices()
    #
    #     # Verifică dacă lista de prețuri este goală
    #     assert len(prices) > 0, "Lista de prețuri este goală."
    #
    #     for i in range(len(prices) - 1):
    #         try:
    #             assert prices[i] <= prices[
    #                 i + 1], f"Lista nu este ordonată crescător la indexul {i}. Elementul {prices[i]} este mai mare decât {prices[i + 1]}."
    #         except AssertionError as e:
    #             env.take_screenshot(
    #                 'Test_for_ascending_price_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
    #             raise e
    #
    # def verify_descending_price(self):
    #
    #     prices = self.get_prices()
    #
    #     # Verifică dacă lista de prețuri este goală
    #     assert len(prices) > 0, "Lista de prețuri este goală."
    #
    #     for i in range(len(prices) - 1):
    #         try:
    #             assert prices[i] >= prices[
    #                 i + 1], f"Lista nu este ordonată descrescator la indexul {i}. Elementul {prices[i]} este mai mic decat {prices[i + 1]}."
    #         except AssertionError as e:
    #             env.take_screenshot(
    #                 'Test_for_descending_price_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")
    #             raise e
    #
    # def select_brand(self, brand_name):
    #     brands_name = self.driver.find_elements(*MainPageLocators.BRANDS_NAME)
    #
    #     for ele in brands_name:
    #         if ele.get_attribute('id') == brand_name.lower():
    #             ele.click()
    #             break

    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIE_ACCEPT_BUTTON).click()
