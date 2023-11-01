from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LiverpoolLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.CSS_SELECTOR, ".ce5b0411e")
        self.error_message = (By.ID, "error-element-password")      

    def enter_credentials(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

    def get_error_message(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.error_message))
            return self.driver.find_element(*self.error_message).text
        except:
            return ""

if __name__ == "__main__":
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://login.liverpool.com.mx/u/login?state=hKFo2SBmUklDeEdBTzAtNjFjRmJqWkFsVmJyVS15aEVJd3gxWqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIENJdUNwRTZjNW80Q2Nld1NUbmh1WFR0Wi0tZDI2aVU3o2NpZNkgVXBQSElJaGNGckRuWVRuUW5pWHFBNjFQN1I4ZERtZGY")

    login_page = LiverpoolLoginPage(driver)
    login_page.enter_credentials("estefaniaconf@gmail.com","T1poscomotu")
    login_page.click_sign_in()
    error_message = login_page.get_error_message()
    if error_message:
        print(f"Error: {error_message}")
    else:
        print("Logged in successfully!")
