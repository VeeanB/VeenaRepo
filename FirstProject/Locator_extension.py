from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH ,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH ,"//form/div[2]/input").send_keys("Test@123")
driver.find_element(By.XPATH ,"//form/div[3]/input").send_keys(("Test@123"))
driver.find_element(By.XPATH ,"//button[@type='submit']").click()
driver.find_element(By.XPATH ,"//button[text()='Save New Password']").click()
