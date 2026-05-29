from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get("https://www.saucedemo.com/")

# Maximize window
driver.maximize_window()

# Wait for page load
time.sleep(2)

# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login button
driver.find_element(By.ID, "login-button").click()

# Wait after login
time.sleep(60)

# Check login success
if "inventory" in driver.current_url:
    print("Login Successful")
else:
    print("Login Failed")

# Take screenshot
driver.save_screenshot("screenshots/login_test.png")

# Close browser
driver.quit()