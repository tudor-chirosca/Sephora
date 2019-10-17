import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from PageObjects.Login import Login
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"
__email__  = "tudorache@gmail.com"


class LoginTest27(unittest.TestCase):
    driver = webdriver.Chrome()
    email_address = "sephoramajor@gmail.com"
    password = "antibacterie"

    @classmethod
    def setUpClass(cls):
        login = Login(cls.driver)
        cls.driver.get(login.url)
        cls.driver.maximize_window()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_27(self):
        login = Login(self.driver)
        login.close_icon()
        login.click_signin()
        login.click_new_to_site()
        element = self.driver.find_elements_by_xpath(Login.password_field)
        if len(element) > 0:
            sys.exit("ERROR. The password field didn't disappear.")
        else:
            print("OK. The password field disappeared.")
        login.click_new_to_site()
        element = self.driver.find_elements_by_xpath(Login.password_field)
        if len(element) > 0:
            print("OK. The password field reappeared.")
        else:
            sys.exit("ERROR. The password field didn't reappear.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="LoginTest27"))
