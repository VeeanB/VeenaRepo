from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://demo.opencart.com/")
driver.maximize_window()
#driver.implicitly_wait(5)
#print(driver.find_element(By.XPATH,"/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").text)

