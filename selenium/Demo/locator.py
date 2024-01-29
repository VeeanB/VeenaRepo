from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
s=Service("C:/geckodriver.exe")

driver = webdriver.Firefox(service=s)
driver.get("https://demo.opencart.com/admin/")
driver.find_element(By.CSS_SELECTOR,"#input-username").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[type=password]").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
print(driver.find_element(By.CSS_SELECTOR,"div.position-fixed").is_displayed())


