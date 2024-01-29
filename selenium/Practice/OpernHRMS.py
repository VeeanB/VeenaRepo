from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

sleep(10)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#driver.find_element(By.XPATH,"//li[2]/a[@class='oxd-main-menu-item active']").click()
sleep(3)
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
sleep(3)
driver.find_element(By.XPATH,"//div[2]/input[@class='oxd-input oxd-input--active']").send_keys("Test")

driver.find_element(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div/div[2]/div/div/div[2]/i").click()
sleep(3)
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[text()='ESS']").click()
wait_ob=WebDriverWait(driver,20)
wait_ob.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@placeholder='Type for hints...']")))
driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Trang")

wait_ob.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Trang')]")))
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Trang')]").click()

driver.find_element(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters'][4]/div/div[2]/div/div/div[2]/i").click()
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Enable')]").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(10)