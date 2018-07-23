import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class SwitchToWindow(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()

    def test_switchToFacebookWindow(self):

        # Locators
        twitterSharingLinkLocator      = "a.wsite-com-product-social-twitter"
        twitterUsernameFieldXPATH      = "//label[@for='username_or_email']"
        twitterPasswordFieldXPATH      = "//label[@for='password']"
        twitterSignInButtonCSS         = "input[type=submit]"
        twitterSubmitButtonID          = "email_challenge_submit"

        # Twitter test account credentials.
        twitterUsername = "tutorys123@gmail.com"
        twitterPassword = "year2014"


        twSharingLinkElement = WebDriverWait(driver, 10).\
            until(lambda driver: driver.find_element_by_css_selector(twitterSharingLinkLocator))

        # Get the main Window handle
        # in order to remember main window we will catch it into variable \
        # before clicking on the button which open a new window. It will be a list of 1 element
        mainWindowHandle = driver.window_handles
        print ("main Window handle: %s" %mainWindowHandle)

        # Click the "Facebook sharing" link, switch to the Facebook login window and log in
        twSharingLinkElement.click()

        # New window will be open now and we need to switch to it. We need to catch all windows in variable\
        # it will be a list on handles. List is not ordered
        allWindowsHandlesList = driver.window_handles
        print ("all window handles: %s" %allWindowsHandlesList)
        # chooshing the new window, by excludidng main window
        for handle in allWindowsHandlesList:
            if handle != mainWindowHandle[0]:
                driver.switch_to.window(handle)
                break

        twitterUsernameFieldElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath(twitterUsernameFieldXPATH))

        twitterPasswordFieldElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath(twitterPasswordFieldXPATH))

        twitterLoginButtonElement = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_css_selector(twitterSignInButtonCSS))

        time.sleep(5)

        twitterUsernameFieldElement.send_keys(twitterUsername)
        twitterPasswordFieldElement.send_keys(twitterPassword)
        twitterLoginButtonElement.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(twitterSubmitButtonID))


    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
