from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Safari driver
driver = webdriver.Safari()

# Navigate to the liverpool.com.mx homepage
driver.get("https://www.liverpool.com.mx/")

# Click on the "Create Account" button
driver.find_element(by=By.XPATH, value="//a[@class='create-account-link']").click()
# driver.find_element_by_xpath("//a[@class='create-account-link']").click()

# Fill in the form
driver.find_element(by=By.ID, value="firstName").send_keys("John")
#driver.find_element_by_id("firstName").send_keys("John")
driver.find_element(by=By.ID, value="lastName").send_keys("Doe")
#driver.find_element_by_id("lastName").send_keys("Doe")
driver.find_element(by=By.ID, value="email").send_keys("johndoe@example.com")
#driver.find_element_by_id("email").send_keys("johndoe@example.com")
driver.find_element(by=By.ID, value="password").send_keys("password123")
#driver.find_element_by_id("password").send_keys("password123")
driver.find_element(by=By.ID, value="confirmPassword").send_keys("password123")
#driver.find_element_by_id("confirmPassword").send_keys("password123")

# Click on the "Create Account" button
driver.find_element(by=By.XPATH, value="//a[@class='create-account-button']").click()
#driver.find_element_by_xpath("//button[@class='create-account-button']").click()

# Wait for the confirmation message to appear
wait = WebDriverWait(driver, 10)
confirmation_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='confirmation-message']")))

# Verify that the account was created successfully
assert confirmation_message.text == "Cuenta creada con éxito. Se ha enviado un correo electrónico de confirmación."

# Sign in with the new account
driver.find_element(by=By.XPATH, value="//*[@id='__next']/header/div[4]/div[2]/div/div/div/div[5]/span").click()
#driver.find_element_by_xpath("//*[@id='__next']/header/div[4]/div[2]/div/div/div/div[5]/span").click()
driver.find_element(by=By.ID, value="username").send_keys("johndoe@example.com")
#driver.find_element_by_id("username").send_keys("johndoe@example.com")
driver.find_element(by=By.ID, value="password").send_keys("password123")
#driver.find_element_by_id("password").send_keys("password123")
driver.find_element(by=By.XPATH, value="//button[@class='sign-in-button']").click()
#driver.find_element_by_xpath("//button[@class='sign-in-button']").click()

# Verify that the user is logged in
assert driver.find_element(by=By.XPATH, value="//a[@class='account-link']").text == "John Doe"
#assert driver.find_element_by_xpath("//a[@class='account-link']").text == "John Doe"

# Close the browser
driver.quit()
