import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
import time


class SwitchToFrame(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        driver.maximize_window()


    def test_switchToFrame(self):
        # Locators
        iFrameID = "iframeResult"
        tryItButtonLocator = "//button[.='Try it']"

        iFrameElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(iFrameID))
        # need to switch focus to iFrame before clicking on button inside of iFrame
        driver.switch_to.frame(iFrameElement)

        tryItButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(tryItButtonLocator))
        tryItButtonElement.click()

        # time.sleep(1)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
