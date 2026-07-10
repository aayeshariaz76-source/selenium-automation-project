from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,20)

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait.until(EC.visibility_of_element_located((By.NAME,"username"))).send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

wait.until(EC.visibility_of_element_located((By.XPATH,"//h6[text()='Dashboard']")))

# Open PIM
driver.find_element(By.XPATH,"//span[text()='PIM']").click()

# Open Add Employee
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Add Employee"))).click()

# Fill Employee Form
wait.until(EC.visibility_of_element_located((By.NAME,"firstName"))).send_keys("Aisha")

driver.find_element(By.NAME,"middleName").send_keys("R")

driver.find_element(By.NAME,"lastName").send_keys("Riaz")

time.sleep(2)

# Screenshot before Save
driver.save_screenshot("AddEmployeeForm.png")

# Click Save
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(8)

# Screenshot after Save
driver.save_screenshot("EmployeeSaved.png")



driver.quit()