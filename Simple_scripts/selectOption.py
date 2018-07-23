from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

import unittest

import time


class selectOption(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()

    def test_selectOption(self):
        # Locators
        dropDownID = "wsite-com-product-option-Quantity"
        dropDownElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_id(dropDownID))

        actions = ActionChains(driver)
        actions.send_keys_to_element(dropDownElement, Keys.ENTER)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        # Just using time.sleep() so that you can see the last webdriver action. I do not recommend using it in your tests
        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
