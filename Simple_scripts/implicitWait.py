from selenium import webdriver

driver = webdriver.Firefox()

driver.implicitly_wait(15)

driver.get("https://www.google.com")

# if webdriver coundn't find webelement the test will fail after 15 minutes with NoSuchElementException
searchField = driver.find_element_by_css_selector("input[name=n]")

driver.quit()