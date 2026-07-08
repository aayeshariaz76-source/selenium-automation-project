from selenium.webdriver.common.by import By
import time

def open_website(driver, url):
    driver.get(url)
    time.sleep(3)


def enter_text(driver, locator, value):
    driver.find_element(By.XPATH, locator).send_keys(value)


def click_button(driver, locator):
    driver.find_element(By.XPATH, locator).click()