
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

Service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://www.globalsqa.com/samplepagetest/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div/form/p/span/input").send_keys("C:/Users/veenu/Downloads/Makup Set.jpg")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div/input").send_keys("Veena")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div[2]/input").send_keys("XYZ@gmail.com")
select = Select(driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div[4]/select"))
select.select_by_visible_text("1-3")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div[5]/label[3]/input").click()

driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div[6]/label[3]/input").click()
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/button").click()
#alert = Alert(driver)
#alert.accept()
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div[7]/textarea").send_keys("COmment here")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/p[3]/button").click()
driver.implicitly_wait(100)
