
# Introduction

This project aims to implement automated tests for the Flip.ro website using Selenium and unittest. 
The primary objectives include simulating user interactions and navigating through the webshop's various functionalities.

- editor code used: pycharm
- version used:
```bash
selenium 4.17.2
webdriver-manager 4.0.1
html-testRunner 1.2.1
```
# Project Structure

The project follows the Page Object Model (POM) design pattern, enhancing modularity and maintainability.
The pages directory encapsulates classes representing specific pages on the Flip.ro website, each handling interactions and elements unique to that page.
For more details about this topics ,you can find [here](https://selenium-python.readthedocs.io/page-objects.html)

![DesignDataBases](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/Captur%C4%83%20de%20ecran%202024-03-05%20212102.png)

- **locators**: Holds locator classes that store all the locators (CSS selectors, XPath ,etc.) used in the project. This separation ensures easy maintenance and updates if the locators change.
```python
from selenium.webdriver.common.by import By
class LoginLocators:
    EMAIL_SELECTOR = (By.CSS_SELECTOR, 'input[autocomplete="current-email"]')
    PASSWORD_SELECTOR = (By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
    GO_TO_MAIN_PAGE = (By.CLASS_NAME, 'btn btn-xs btn-primary  ')
    LOGIN_BUTTON = (By.XPATH, '//span[contains(text(), "Acceseaza cont")]')
    ERROR_MESSAGE_FOR_AUTHENTIFICATION = (By.XPATH, '//div[@class="toasted bubble error"]')
    ACCOUNT_SIDE_MENU_BAR = (By.CLASS_NAME, 'menu-item')
    LOGOUT_SUCCES_MESSAGE = (By.XPATH, '//div[@class="toasted bubble success"]')
 ```
 ```python
from selenium.webdriver.common.by import By
class SearchLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, 'div.navbar-search>section>fieldset>div>input')
    PRODUCTS_ITEM = (By.CLASS_NAME, 'card-phone-new position-relative d-flex flex-md-column')
    PRICE_PRODUCTS_ITEM = (By.XPATH, '//div[@data-cy="phone-real-price"]')
    PRODUCT_ITEM_TITLE = (By.XPATH, '//div[@data-cy="phone-title"]')
    FILTER_MESSAGE_TITLE = (By.XPATH, '//div[@class="d-flex justify-content-around container"] //h3')
    PRICE_SLIDER_FILTER = (By.XPATH, '//div[@aria-valuetext="8550"]')
 ```
- **pages**: Contains classes representing specific pages on the Flip.ro website. Each class encapsulates interactions and elements unique to that page.
 ```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Locators.Login_pages_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, user_email):
        email = self.driver.find_element(*LoginLocators.EMAIL_SELECTOR)
        email.clear()
        email.send_keys(user_email)

    def SetPassword(self, user_password):
        password = self.driver.find_element(*LoginLocators.PASSWORD_SELECTOR)
        password.clear()
        password.send_keys(user_password)

    def ClickSubmitButton(self):
        click_button = self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        click_button.click()

    def Get_error_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE_FOR_AUTHENTIFICATION)).text
 ```
__init__(self, driver): The class constructor that initializes the driver attribute, representing the Selenium WebDriver.

In this class, we have methods for setting an email, a password, clicking the submit button, and a method that waits for the visibility of the error message, returning its text and others. These methods are designed to be utilized further in the test class.

This class uses intelligent waits, such as WebDriverWait and expected_conditions, to ensure synchronization between automated actions and the actual state of the web page. It also imports the LoginLocators class from the Locators module to centrally manage and organize locators specific to the login page



# Tehnical information





# Feature under the tests

 ## Login Functionality Testing:

- Validate login with correct credentials.
- Test login with correct username and incorrect password.
- Test login with a short password.
- Test login with wrong credentials.
- Test login with an incorrect email format.
- Test login without completing any field.
- Test login without completing the password field.

## Search Functionality Testing:

- Verify product search functionality.
- Test searching for a product that exists.
- Test searching for a product that doesn't exist.
- Test filtering search results by price range.

# Getting Started

Clone the repository.

```git
  git clone https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject.git
```

Install the required dependencies.

```git
pip install -r requirements.txt
```

Run the test suite using the provided runner.


# Usage

Execute the automated tests to verify the Flip.ro website's login and search functionalities.






