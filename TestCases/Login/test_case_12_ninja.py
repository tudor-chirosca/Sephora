import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.LoginNinja import LoginNinja
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class LoginTest12Ninja(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "jacknicholson@gmail.com"
    password = "123456789"
    @classmethod
    def setUpClass(cls):
        login = LoginNinja(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_12_ninja(self):
        login = LoginNinja(self.driver)
        login.click_my_account_link()
        login.click_login_link()
        login.set_email(self.email_address)
        login.set_password(self.password)
        login.click_login_button()
        time.sleep(1)
        login.click_my_account_link()
        login.click_logout()
        login.windows_back_page()
        time.sleep(1)
        login.click_edit_account()
        element = self.driver.find_element_by_xpath(LoginNinja.new_customer_text).is_displayed()
        if element:
            print("OK. The user wasn't logged out.")
        else:
            sys.exit("ERROR. The user was logged out.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest12Ninja"))
