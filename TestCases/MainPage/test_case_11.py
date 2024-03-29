import unittest
import HtmlTestRunner
from PageObjects.MainPage import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MainPageTest11(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_11(self):
        wait = WebDriverWait(self.driver, 10)
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Click on "About Sephora" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.about_sephora_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_about_sephora)))
        assert element.is_displayed(), "ERROR. 'About Sephora' page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on "Careers" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.careers_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_careers_link)))
        assert element.is_displayed(), "ERROR. 'Careers' page wasn't opened."
        # Click back button on browser
        main.browser_back_button()
        # Click on "Sephora Stands Social Impact" link (bottom of the page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, MainPage.social_impact_link)))
        element.click()
        # Verify if the right page was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, MainPage.verify_social_impact)))
        assert element.is_displayed(), "ERROR. 'Sephora Stands Social Impact' page wasn't opened."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest11"))
