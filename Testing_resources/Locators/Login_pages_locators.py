from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_SELECTOR = (By.CSS_SELECTOR, 'input[autocomplete="current-email"]')

    PASSWORD_SELECTOR = (By.CSS_SELECTOR, 'input[autocomplete="current-password"]')

    GO_TO_MAIN_PAGE = (By.CLASS_NAME, 'btn btn-xs btn-primary')

    LOGIN_BUTTON = (By.XPATH, '//span[contains(text(), "Acceseaza cont")]')

    TOAST_MESSAGE_ERROR_FOR_AUTHENTIFICATION = (By.XPATH, '//div[@class="toasted bubble error"]')

    TOAST_MESSAGE_FOR_SUCCES_LOGOUT = (By.XPATH, '//div[@class="toasted bubble success"]')


