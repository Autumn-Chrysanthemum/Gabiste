from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.google.com")

fLocator = "input[name=q]"

try:
    # webdriver will wait for max 10 sec, if element during this time present on the page - will return element. Otherwise TimeoutException thrown
    searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))
finally:
    driver.quit()


