from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LiverpoolLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.XPATH, '//*[@id="__next"]/header/div[4]/div[2]/div/div/div/div[5]/span')
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.CSS_SELECTOR, ".ce5b0411e")
        self.error_message = (By.ID, "error-element-password")
        
    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.username_input))

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
    driver.get("https://www.liverpool.com.mx/tienda/home")

    login_page = LiverpoolLoginPage(driver)
    driver.find_element(By.XPATH, '//*[@id="__next"]/header/div[4]/div[2]/div/div/div/div[5]').click()
    WebDriverWait(driver, 30)