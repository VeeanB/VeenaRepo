from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul/li[2]/a").text)
driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div/div[4]/div[2]/div[4]/div/div/div[3]/div[2]/button[1]").click()
driver.implicitly_wait(10)