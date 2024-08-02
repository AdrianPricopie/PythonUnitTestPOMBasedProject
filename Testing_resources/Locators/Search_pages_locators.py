from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_BAR = (By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[2]/div/div/input')
    PRODUCTS_ITEM = (By.CLASS_NAME, 'card-phone-new position-relative d-flex flex-md-column')
    PRICE_PRODUCTS_ITEM = (By.XPATH, '//div[@data-cy="phone-real-price"]')
    PRODUCTS_ITEM_TITLE = (By.XPATH, '//div[@data-cy="phone-title"]')
    FILTER_MESSAGE_TITLE = (By.XPATH, '//div[@class="d-flex justify-content-around container"] //h3')
    PRICE_SLIDER_FILTER = (By.XPATH, '//div[@aria-valuetext="8040"]')
    COOKIE_ACCEPT_BUTTON = (By.XPATH, '//span[contains(text(), "Da, sunt de acord")]')
    COLOR_FILTRE = (By.CSS_SELECTOR, 'div[class="btn-color-containe"]')
    PRICE_RADIO_BUTTON_FILTER = (By.CSS_SELECTOR, 'input[type="radio"] +label ')
    RESULT_MESSAGE_FOR_TERM = (By.CSS_SELECTOR,'h1[class="text-[#231F20] text-sm tablet2:text-lg"]')
    RESULT_MESSAGE_FOR_COUNT_TERM = (By.CSS_SELECTOR, 'div[class="inline-block tablet2:p-[6px] tablet2:bg-gray-background tablet2:rounded"]')
    SEARCH_SUGGESTIONS = (By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div')

