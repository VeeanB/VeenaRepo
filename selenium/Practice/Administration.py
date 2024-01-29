from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://demo.opencart.com/admin/")
driver.find_element(By.XPATH,"/html/body//div[1]/div/div/div/div/div/div[2]/form/div/div/input").send_keys("admin")
driver.find_element(By.XPATH,"//html/body//div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input").send_keys("admin123")
driver.find_element(By.XPATH,"/html/body//div[1]/div/div/div/div/div/div[2]/form/div[3]/button").click()
print(driver.find_element(By.XPATH,"/html/body/div[1]/footer/a").text)
