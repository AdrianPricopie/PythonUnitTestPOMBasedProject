# Automated Testing Project for Flip.ro Website :computer:
Welcome to the documentation for the automated testing project designed for the Flip.ro website. This project leverages Selenium and the unittest framework to implement a robust suite of tests, ensuring the functionality and reliability of Flip.ro's webshop.
## Table of Contents

1. [Introduction/Tools and version](#introduction-notebook)
2. [Project Structure](#project-structure)
3. [Features Under Testing](#feature-under-the-tests)
    - [Login Functionality Testing](#feature-under-the-tests)
    - [Search Functionality Testing](#search-functionality-testing)
4. [Getting-Started](#getting-started--pushpin)
6. [Usage](#usage)
7. [Reports](#reports)
8. [Conclusion](#conclusions)


# Introduction :notebook:

This project aims to implement automated tests for the Flip.ro website using Selenium and unittest. 
The primary objectives include simulating user interactions and navigating through the webshop's various functionalities.

- **editor code used: pycharm**
- **Library Versions:**
    ```bash
     selenium==4.17.2
    webdriver-manager==4.0.1
    html-testRunner==1.2.1
    allure-pytest==2.13.5
    assertpy==1.1
    ```
# Project Structure

The project follows the Page Object Model (POM) design pattern, enhancing modularity and maintainability.
The pages directory encapsulates classes representing specific pages on the Flip.ro website, each handling interactions and elements unique to that page.
For more details about this topics ,you can find [here](https://selenium-python.readthedocs.io/page-objects.html)

![Project Structure](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/ScreenshotsForGit/Screenshot%202024-04-05%20at%2015.53.00.png)


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
from Testing_resources.Locators.Login_pages_locators import LoginLocators


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
import unittest
from datetime import datetime
from selenium import webdriver
from Testing_resources.pages.login_pages import LoginPage as LP
from Testing_resources.Utils.UtilsDataForTests import DataTest
```

unittest: A module that provides a **testing framework**, allowing the creation and execution of test cases.

datetime: Offers classes for working with dates and times. In this context, it  be used datetime to append a timestamp to the screenshot filename to ensure each screenshot has a unique identifier, making it easier to organize and identify captured images:

webdriver: Part of the Selenium library, this module provides an API for interacting with web browsers.

LP (LoginPage): Alias for the LoginPage class from the pages.login_pages module. Represents the **page object for the login functionality.**

Selector (LoginLocators): Alias for the LoginLocators class from the Locators.Login_pages_locators module. Contains locators specific to the login page.

Utils.UtilsDataForTests importing some test data. It's quite common to have utilities that provide test data or helper functions for test automation.

```python
class DataTest:
    correct_email = 'Test123z@yahoo.com'
    short_pass = 'Testc'
    wrong_pass = 'Testcdsad2@'
    correct_pass = 'Test123'
    wrong_format_email = 'Test123zyahoo.com'
    wrong_email = 'Grigore@yahoo.com'
    items_pressent_in_login_dashboard = ['Cumparaturile mele', 'Vanzarile mele', 'Garantiile mele', 'Asigurarile mele',
                                         'Retur',
                                         'Setari cont', 'Logout']

    product_name = 'iPhone 13'
    inexisting_product = 'fdsafdasfd'
    interval_cautare = (200, 3280)
```

EC (expected_conditions): A module providing a set of predefined conditions to use with WebDriverWait. These conditions are used for intelligent waits in synchronization with the web page state.

WebDriverWait: A class in Selenium that allows waiting for certain conditions to be met before proceeding. It's often used with expected_conditions for synchronization
```python

class TestLoginFeature(unittest.TestCase):

    def setUp(self):
        # Setting up the WebDriver and navigating to the login page

        self.driver = webdriver.Chrome()
        self.driver.get('https://flip.ro/autentifica-te/')
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)
        # Creating an object for the LoginPage class, which
        # contains the necessary methods for the login page
        self.LoginPage = LP(self.driver)

        # Accepting cookies
        self.LoginPage.accept_cookies()

        # Create an object for the DataTest class,which contains the necessary test data
        self.DataTest = DataTest

    def tearDown(self):
        # Closing the browser after each test
        self.driver.quit()
```
This code defines a unit test for the login functionality on the website https://flip.ro/autentifica-te/. The setUp method is used to prepare the testing environment, and tearDown is used to clean up the testing environment after the test is finished.

The setUp method is called before each test to prepare the testing environment. Here's what it does:

It opens a new web browser (in this case, Chrome) using Selenium WebDriver and navigates to the login page of the website https://flip.ro/autentifica-te/.
The browser window is maximized to ensure a consistent testing experience.
implicitly_wait(5) sets a maximum implicit wait time of 5 seconds to find elements on the page.
An object is created for the LoginPage class (assuming it was previously imported with the alias LP), which contains the necessary methods for the login page.
It accepts cookies using the accept_cookies() method from the LoginPage class.
An object is created for the DataTest class, which contains the necessary test data.


This **test case**, named test_login_without_complete_password_field, is a part of a broader test suite designed to validate the login functionality on a website. The test begins by setting the email field with a correct email address and proceeds to click the submit button on the login page. Subsequently, it captures the actual error message displayed on the page after attempting to login without providing a password and compares it with the expected error message, which is "Parola lipsește." (Password is missing). If the actual and expected error messages do not match, an AssertionError is raised. In case of failure, the test captures a screenshot of the page, saves it with a timestamped filename, and raises an AssertionError with a descriptive message indicating the failure along with the path to the saved screenshot. This test ensures that the appropriate error message is shown when attempting to login without entering a password, thus validating the expected behavior of the login functionality.

- **reports**: Automatically generated HTML reports after each test suite run. These reports provide detailed information about the test results.
- **screenshots**: Automatically captured screenshots for failed test cases. These images are helpful for identifying and debugging issues.
- **venv**:

## Getting Started  :pushpin:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject.git
    ```

2. **Navigate to the project directory:**
    
    ```bash
    cd PythonUnitTestPOMBasedProject
    ```

3. **Create venv:**
    
    ```bash
    python -m venv venv
    ```
    
4. **Install Dependencies:**

    ```bash
    pip install -r requirments.txt
    ```

5. **Activate the Virtual Environment:**

    for mac

    ```Terminal
    source venv/bin/activate         

    ```
   for windows 
    
    ```Terminal
     venv/Scripts/Activate  
    ```
    
6. **Run the Test Suite with html reports:**

    ```bash
    python -m unittest Test_Suite.py
    ```
    
# Usage

Execute the automated tests to verify the Flip.ro website's login and search functionalities.


# Reports

The project includes HTML reports generated after each test suite run, offering detailed insights into test results. The reports provide a clear overview of the tested functionalities, making it easy to identify any issues that may arise during testing.

- Below, you can see the report generated on March 5, 2024, for the sogin and search functionality

![TestReport Login](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/ScreenshotsForGit/TestReportLogin.png)
![TestReport Login](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/ScreenshotsForGit/TestReportSearch.png)

-Below,you can see the combine report generated on March 22,2024 for the login and search functionality

![TestReport Login](https://github.com/AdrianPricopie/PythonUnitTestPOMBasedProject/blob/master/ScreenshotsForGit/Report_Combine_2024.png)

All the tests are passed.

# Conclusions

In conclusion, the automated testing project for the Flip.ro website has been successfully implemented using Selenium and the unittest framework. The Page Object Model (POM) design pattern was employed to enhance modularity and maintainability, allowing for efficient management of locators, pages, and test scripts.

The project covers critical functionalities such as login and search, with a focus on various test scenarios to ensure robustness. The tests are organized into a structured project layout, including locators, pages, tests, reports, screenshots, and a virtual environment. The project also provides clear documentation on how to clone the repository, install dependencies, activate the virtual environment, and run the test suite

Automated tests have been designed to cover a range of scenarios, including positive and negative cases for the login functionality, as well as comprehensive testing of the search functionality. Screenshots are captured for failed test cases, providing visual aids for debugging and issue identification.

In the future, the project can be expanded to cover additional functionalities and scenarios, ensuring continuous testing and validation of the Flip.ro webshop. Regular maintenance and updates to locators and test scripts will be crucial as the website evolves.


