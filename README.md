# Automated Testing Project for Flip.ro Website :computer:
Welcome to the documentation for the automated testing project designed for the Flip.ro website. This project leverages Selenium and the unittest framework to implement a robust suite of tests, ensuring the functionality and reliability of Flip.ro's webshop.
## Table of Contents

1. [Introduction/Tools and version](#tools-and-versions)
2. [Project Structure](#project-structure)
    - [Locators](#locators)
    - [Pages](#pages)
    - [Tests](#tests)
    - [Reports, Screenshots, venv, Requirements.txt](#directories-and-files)
    - [Test Suite Script](#test-suite-script)
3. [Features Under Testing](#features-under-testing)
    - [Login Functionality Testing](#login-functionality-testing)
    - [Search Functionality Testing](#search-functionality-testing)
4. [Getting Started](#getting-started)
    - [Clone the Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Run the Test Suite](#run-the-test-suite)
5. [Conclusion](#conclusion)


# Introduction :notebook:

This project aims to implement automated tests for the Flip.ro website using Selenium and unittest. 
The primary objectives include simulating user interactions and navigating through the webshop's various functionalities.

- **editor code used: pycharm**
- **Library Versions:**
    ```bash
     selenium 4.17.2
     webdriver-manager 4.0.1
     html-testRunner 1.2.1
    ```
# Project Structure

The project follows the Page Object Model (POM) design pattern, enhancing modularity and maintainability.
The pages directory encapsulates classes representing specific pages on the Flip.ro website, each handling interactions and elements unique to that page.
For more details about this topics ,you can find [here](https://selenium-python.readthedocs.io/page-objects.html)



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
        email.send_keys(user_email)

    def SetPassword(self, user_password):
        password = self.driver.find_element(*LoginLocators.PASSWORD_SELECTOR)
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

- **tests**: Contains the test scripts organized based on functionalities. Currently, you have the `LoginTest` and `Search_user_test` directories.
  
These imports are used in the login test file and serve different purposes:
```python
import time
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_pages import LoginPage as LP
from Locators.Login_pages_locators import LoginLocators as Selector
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
```
time: Used for introducing delays in the test execution, providing a pause between actions.

unittest: A module that provides a **testing framework**, allowing the creation and execution of test cases.

datetime: Offers classes for working with dates and times. In this context, it  be used datetime to append a timestamp to the screenshot filename to ensure each screenshot has a unique identifier, making it easier to organize and identify captured images:

webdriver: Part of the Selenium library, this module provides an API for interacting with web browsers.

By: Enumerations used by the expected_conditions module to specify the way in which elements should be located.

LP (LoginPage): Alias for the LoginPage class from the pages.login_pages module. Represents the **page object for the login functionality.**

Selector (LoginLocators): Alias for the LoginLocators class from the Locators.Login_pages_locators module. Contains locators specific to the login page.

EC (expected_conditions): A module providing a set of predefined conditions to use with WebDriverWait. These conditions are used for intelligent waits in synchronization with the web page state.

WebDriverWait: A class in Selenium that allows waiting for certain conditions to be met before proceeding. It's often used with expected_conditions for synchronization
```python
class TestLoginFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page

        self.driver = webdriver.Chrome()
        self.driver.get('https://flip.ro/autentifica-te/')
        self.driver.maximize_window()

        # Accepting cookies

        self.driver.find_element(By.XPATH, '//span[contains(text(), "Da, sunt de acord")]').click()
        self.driver.implicitly_wait(5)
        self.LoginPage = LP(self.driver)

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()
```
This code sets up and tears down the WebDriver for the login feature tests. In the setUp method, it initializes the WebDriver, navigates to the login page, accepts cookies, and creates an instance of the LoginPage class. The tearDown method closes the browser after each test.

```python
 def test_login_without_complete_password_field(self):
        self.LoginPage.SetEmail('Bobita123@yahoo.com')
        self.LoginPage.ClickSubmitButton()
        actual_result = self.LoginPage.Get_error_message()
        expected_result = 'Parola lipsește.'
        try:
            self.assertEqual(actual_result, expected_result,
                             f"the {actual_result} doesn't correspond to the expected result")
        except AssertionError:
            # Capture and save screenshot in case of failure
            screenshot_name = 'C:/Users/adi_d/PycharmProjects/ProiectUnitTestExamen/screenshots/' + 'Error_message_for_login' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'

            self.driver.get_screenshot_as_file(screenshot_name)

            # Raise AssertionError without traceback information
            raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')
```
Below is a type of test from the 8 tests in this class. This test case checks the behavior of the login functionality when the password field is left incomplete. This is a negative testing scenario (logging in without completing the password field). The test sets an email, clicks the submit button, captures the actual error message, and compares it with the expected result ('Parola lipsește.'). If the actual and expected results don't match, an AssertionError is raised. In case of failure, a screenshot is captured and saved with a timestamp in the filename for identification. The test result, along with the captured screenshot, is then reported.

- **reports**: Automatically generated HTML reports after each test suite run. These reports provide detailed information about the test results.
- **screenshots**: Automatically captured screenshots for failed test cases. These images are helpful for identifying and debugging issues.
- **venv**: The virtual environment directory.
- **requirements.txt**: Lists all the required dependencies for the project. Install these dependencies before running the tests.
- **test_suite.py**: Script to run the entire test suite using the provided runner.

## Feature under the tests

 ### Login Functionality Testing:
1. Validate login with correct credentials.
2. Test login with correct username and incorrect password.
3. Test login with a short password.
4. Test login with wrong credentials.
5. Test login with an incorrect email format.
6. Test login without completing any field.
7. Test login without completing the password field.


### Search Functionality Testing:

8. Verify product search functionality.
9. Test searching for a product that exists.
10. Test searching for a product that doesn't exist.
11. Test filtering search results by price range.

## Getting Started  :pushpin:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Activate the Virtual Environment:**

    ```bash
    venv/Scripts/Activate
    ```

4. **Run the Test Suite:**

    ```bash
    python -m unittest Test_Suite.py
    ```



# Usage

Execute the automated tests to verify the Flip.ro website's login and search functionalities.


# Reports

The project includes HTML reports generated after each test suite run, offering detailed insights into test results. The reports provide a clear overview of the tested functionalities, making it easy to identify any issues that may arise during testing.

- Below, you can see the report generated on March 5, 2024, for the Login and Search Functionality

![TestReport Login](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/TestReportLogin.png)
![TestReport Login](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/TestReportSearch.png)


# Conclusions

In conclusion, the automated testing project for the Flip.ro website has been successfully implemented using Selenium and the unittest framework. The Page Object Model (POM) design pattern was employed to enhance modularity and maintainability, allowing for efficient management of locators, pages, and test scripts.

The project covers critical functionalities such as login and search, with a focus on various test scenarios to ensure robustness. The tests are organized into a structured project layout, including locators, pages, tests, reports, screenshots, and a virtual environment. The project also provides clear documentation on how to clone the repository, install dependencies, activate the virtual environment, and run the test suite

Automated tests have been designed to cover a range of scenarios, including positive and negative cases for the login functionality, as well as comprehensive testing of the search functionality. Screenshots are captured for failed test cases, providing visual aids for debugging and issue identification.

In the future, the project can be expanded to cover additional functionalities and scenarios, ensuring continuous testing and validation of the Flip.ro webshop. Regular maintenance and updates to locators and test scripts will be crucial as the website evolves.


