from datetime import datetime
from Testing_resources.Locators.My_account_locators import MyAccountLocators as Locators
from Testing_resources.Locators.My_account_locators import MyAccountLocators
from assertpy import assert_that
from Testing_resources.Utils.Environment import Environment as env


class MyAccount_page:

    def __init__(self, driver):
        self.driver = driver
        self.env = env(self.driver)

    def get_title_account_name(self):
        title = self.driver.find_element(*Locators.ACCOUNT_NAME).text
        return title

    def verify_title_name_in_my_account(self,expected_message,test_name):
        actual_result = self.get_title_account_name()
        expected_result = expected_message
        try:
            assert_that(actual_result).described_as(
                f"the {actual_result} doesn't correspond to the expected result").is_equal_to(expected_result)
        except AssertionError as e:
            self.env.take_screenshot(
                f'{test_name}_failure' + '_' + datetime.now().strftime('%d-%m-%Y') + "_")

            raise e



    def Get_account_side_menu_bar(self):
        menu_list_item = self.driver.find_elements(*MyAccountLocators.ACCOUNT_SIDE_MENU_BAR)
        element_actual_text = []
        for element in menu_list_item:
            element_actual_text.append(element.text)
        return element_actual_text

    def verify_elements_in_account_present(self, expected_elements, test_name):
        actual_elements = self.Get_account_side_menu_bar()
        try:
            for expected_element in expected_elements:
                assert_that(actual_elements).described_as(
                    f"Elementul '{expected_element}' lipsește din meniu, {actual_elements}."
                ).contains(expected_element)
        except AssertionError as e:
            screenshot_name = f'{test_name}_failure_' + datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
            self.env.take_screenshot(screenshot_name)
            raise e

