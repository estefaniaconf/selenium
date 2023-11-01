import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['PATH'] += r"/usr/bin/safaridriver"
driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://www.liverpool.com.mx/tienda/home")
driver.implicitly_wait(30)

search_bar = driver.find_element(By.ID, "mainSearchbar")
search_bar.send_keys("Barbie")
time.sleep(0.2)
search_bar.send_keys(Keys.ENTER)