from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class WaitForElements(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://travelingtony.weebly.com")

    def test_AssertTitle(self):
        self.assertEqual(driver.title, "Traveling Tony's Photography - Welcome")

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
