import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SwitchToWindow(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p3/Asala_Loadge.html")
        driver.maximize_window()

    def test_switchToFacebookWindow(self):

        # Locators
        facebookSharingLinkLocator      = "a.wsite-com-product-social-facebook"
        facebookUsernameFieldID         = "email"
        facebookPasswordFieldID         = "pass"
        facebookLoginButtonName         = "login"
        facebookShareLinkButtonXpath    = "//span[contains(text(), 'Post to Facebook')]"

        # Facebook credentials.
        facebookUsername = "tutorys123@gmail.com"
        facebookPassword = "year2014"

        fbSharingLinkElement = WebDriverWait(driver, 10).\
            until(lambda driver: driver.find_element_by_css_selector(facebookSharingLinkLocator))

        # Get the main Window handle
        # in order to remember main window we will catch it into variable \
        # before clicking on the button which open a new window. It will be a list of 1 element
        mainWindowHandle = driver.window_handles
        print ("main Window handle: %s" %mainWindowHandle)

        # Click the "Facebook sharing" link, switch to the Facebook login window and log in
        fbSharingLinkElement.click()

        # New window will be open now and we need to switch to it. We need to catch all windows in variable\
        # it will be a list on handles. List is not ordered
        allWindowsHandlesList = driver.window_handles
        print ("all window handles: %s" %allWindowsHandlesList)
        # chooshing the new window, by excludidng main window
        for handle in allWindowsHandlesList:
            if handle != mainWindowHandle[0]:
                driver.switch_to.window(handle)
                break

        facebookUsernameFieldElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_id(facebookUsernameFieldID))

        facebookPasswordFieldElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_id(facebookPasswordFieldID))

        facebookLoginButtonElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_name(facebookLoginButtonName))

        facebookUsernameFieldElement.send_keys(facebookUsername)
        facebookPasswordFieldElement.send_keys(facebookPassword)
        facebookLoginButtonElement.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(facebookShareLinkButtonXpath))


    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
