
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






