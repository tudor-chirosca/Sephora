import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class LoginTest12Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"

    @classmethod
    def setUpClass(cls):
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_12_ninja(self):
        login = LoginNinja(self.driver)
        # Click "My Account" link
        login.click_my_account_link()
        # Click "Login" link
        login.click_login_link()
        # Enter valid email
        login.set_email(self.email_address)
        # Enter valid password
        login.set_password(self.password)
        # Click "Login" button
        login.click_login_button()
        # Click "My Account" link
        login.click_my_account_link()
        # Click "Logout" link
        login.click_logout()
        # Click "Back Arrow" button (browser)
        login.windows_back_page()
        # Click "Edit Account" link
        login.click_edit_account()
        # Verify if user is logged out (must be logged out, else => error)
        element = self.driver.find_element_by_xpath(LoginNinja.new_customer_text).is_displayed()
        assert element, "ERROR. The user was logged out."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest12Ninja"))
