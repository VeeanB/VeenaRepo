from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/form/div/input").send_keys("Admin")
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/form/div[2]/input").send_keys("admin123")
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/form/input").click()
print(driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/h4").text)