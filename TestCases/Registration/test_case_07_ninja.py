import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.RegisterNinja import RegisterNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest003Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    first_name = "Jack"
    last_name = "Nicholson"
    email = "jacknicholson@gmail.com"
    telephone = "12122256998"
    password = "123456789"
    password_confirm = "123456789"

    @classmethod
    def setUpClass(cls):
        reg = RegisterNinja(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(reg.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_07_ninja(self):
        reg = RegisterNinja(self.driver)
        # Click on "My Account" link
        reg.click_my_account_link()
        # Click on "Register" link
        reg.click_register_link()
        # In "First name" field enter an existing First name
        reg.set_first_name(self.first_name)
        # In "Last name" field enter an existing Last name
        reg.set_last_name(self.last_name)
        # In "Email address" field enter a valid email address
        reg.set_email(self.email)
        # In "Telephone" field enter a valid telephone
        reg.set_telephone(self.telephone)
        # In "Password" field enter a valid password
        reg.set_password(self.password)
        # In "Password Confirm" field repeat the password
        reg.set_password_confirm(self.password_confirm)
        # Check "Privacy Policy" checkbox
        reg.click_privacy_policy_checkbox()
        # Click "Continue" button
        reg.click_continue_button()
        time.sleep(1)
        # Verify that system generates a validation error message when entering existing email
        element = self.driver.find_element_by_xpath(RegisterNinja.warning_email).is_displayed()
        if element:
            print("OK. A warning message was displayed.")
        else:
            sys.exit("ERROR. No warning message was displayed.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="RegisterTest07Ninja"))
