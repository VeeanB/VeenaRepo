from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
#browser.get("https://www.google.com")
driver.get("https://demo.opencart.com/admin/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#input-username").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[type=password]").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
print(driver.find_element(By.CSS_SELECTOR,"div.position-fixed").text)
