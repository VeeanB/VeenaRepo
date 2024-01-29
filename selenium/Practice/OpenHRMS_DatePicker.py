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

sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(4)
driver.find_element(By.XPATH,"//span[text()='Leave']").click()
sleep(10)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").click()
driver.find_element(By.XPATH,"//li[@class='oxd-calendar-selector-year']/div/p").click()
years=driver.find_elements(By.XPATH,"//li[contains(@class,'oxd-calendar-dropdown--option')or(contains(@class,'oxd-calendar-dropdown--option --selected'))]")
for i in years:
    if i.text=="1999":
        i.click()
        break

driver.find_element(By.XPATH,"//div[@class='oxd-calendar-selector-month-selected']/p").click()
months=driver.find_elements(By.XPATH,"//li[contains(@class,'oxd-calendar-dropdown--option') or (contains(@class,'oxd-calendar-dropdown--option --selected'))]")
for i in months:
    print(i.text)
    if i.text=="May":
        i.click()
        break
dates=driver.find_elements(By.XPATH,"//div[@class='oxd-calendar-dates-grid']/div")
for i in dates:
     if i.text=='20':
         i.click()
         break
sleep(5)
print(driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[1]/input").get_attribute("value"))