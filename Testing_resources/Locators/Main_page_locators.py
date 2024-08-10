from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIE_ACCEPT_BUTTON = (By.XPATH, '//span[contains(text(), "Da, sunt de acord")]')

    GO_TO_PRODUCT_LIST_PAGE_BUTTON = (By.CLASS_NAME, 'btn btn-xs btn-primary')

