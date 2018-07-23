import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time


class SwitchToAlert(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.tizag.com/javascriptT/javascriptconfirm.php")
        driver.maximize_window()

    def test_switchToAlert(self):

        # Locators
        leaveButtonLocator = "//input[@value='Leave Tizag.com']"

        leaveButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(leaveButtonLocator))
        leaveButtonElement.click()

        # alert will be displayed and we need to switch to alert
        alert = driver.switch_to.alert

        # to accept
        alert.accept()

        # to dismiss
        # alert.dismiss()

        # time.sleep(5)

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
