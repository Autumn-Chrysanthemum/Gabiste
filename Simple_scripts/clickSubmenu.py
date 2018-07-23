import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ClickSubmenu(unittest.TestCase):

    def setUp(self):
        global driver
        driver= webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/")

        # TODO: FIND RIGHT LOCATOR. WE HAVE DINAMIC MENU HERE:
        # driver.get("https://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")

        driver.maximize_window()


    def test_clickSubmenu(self):
        # Locators
        africaMenuLocator = "//a[.='Africa']"
        gabonSubmenuLocator   = "//a[contains(@href, 'gabon')]"
        impalaDivLocator      = "//div[@class='wsite-header']"
        africaMenuElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(africaMenuLocator))

        actions = ActionChains(driver)
        actions.move_to_element(africaMenuElement)
        actions.click(driver.find_element_by_xpath(gabonSubmenuLocator))
        actions.perform()

        WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath(impalaDivLocator))

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
