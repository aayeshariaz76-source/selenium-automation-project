from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

    # Intentionally wrong username and password
    driver.find_element(By.NAME, "username").send_keys("WrongUser")
    driver.find_element(By.NAME, "password").send_keys("WrongPassword")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    print("Test Failed - Screenshot Captured")

    driver.save_screenshot("Login_Failure.png")

except Exception as e:
    print(e)

finally:
    input("Press Enter to close browser...")
    driver.quit()