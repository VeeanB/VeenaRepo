from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()

# driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div/div/form/div[2]/div/input").send_keys("admin@yourstore.com")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div/div/form/div[2]/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div/div/form/div[3]/button").click()
# driver.implicitly_wait(10)
# print(driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div/div/form/input[2]").text)   # Text is not printing here

driver.get("https://demoqa.com/modal-dialogs")
driver.find_element(By.ID,"showSmallModal").click()
driver.find_element(By.XPATH,"//button[@id='closeSmallModal']").click()
driver.find_element(By.ID,"showLargeModal").click()
driver.find_element(By.ID,"closeLargeModal").click()