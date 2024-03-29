import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common import action_chains
from PageObjects.MainPage import MainPage
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Sephora")

__author__ = "Tudor C"


class MainPageTest18(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        main = MainPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(main.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mainpage_18(self):
        main = MainPage(self.driver)
        main.click_close_x_icon()
        # Mouseover "SHOP" dropdown box
        # Click on "HAIR" link box
        actions = action_chains.ActionChains(self.driver)
        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        actions.move_to_element(shop).perform()
        hair = self.driver.find_element_by_xpath(MainPage.hair_link)
        actions.move_to_element(hair).perform()
        hair.click()
        # Verify if the right page was opened
        assert self.driver.title == "Hair Care Products | Sephora", "ERROR. Hair Care Products page wasn't opened."
        # Go back to the main page
        main.click_main_page()
        # Mouseover "SHOP" dropdown box
        # Click "TOOLS & BRUSHES" link box
        actions = action_chains.ActionChains(self.driver)
        shop = self.driver.find_element_by_xpath(MainPage.mouseover_shop)
        actions.move_to_element(shop).perform()
        tools_brushes = self.driver.find_element_by_xpath(MainPage.tools_brushes_link)
        actions.move_to_element(tools_brushes).perform()
        tools_brushes.click()
        # Verify if the right page was opened
        assert self.driver.title == "Makeup Tools, Beauty Tools & Makeup Accessories | Sephora", "ERROR. Makeup Tools, Beauty Tools & Makeup Accessories page wasn't opened."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Sephora\\Reports",
        report_name="MainPageTest18"))
