import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver instance
os.environ['PATH'] += r"/usr/bin/safaridriver"
driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://www.liverpool.com.mx/tienda/home")

class SearchBar:
    def __init__(self, driver):
        self.driver = driver
    def main_search_bar(self, article):
        self.driver.find_element(By.ID, "mainSearchbar").send_keys(article)
    def lookup (self):
        self.driver.find_element(By.ID, "icon-zoom").click()
    
class LeftMenu:
    def __init__(self, driver):
        self.driver = driver
    def categorias (self):
        self.driver.find_element(By.LINK_TEXT, "Categorías")