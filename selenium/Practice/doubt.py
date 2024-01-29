from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/ajax.html")
#driver.find_element(By.XPATH,"//input[@id='yes']").click()
# ele =driver.find_elements(By.XPATH,"//input[@type='radio']")
# print(len(ele))
# print(ele)
# for i in ele:
#     print(i.text)

#for radio button its not working
#***************************************************************************************
ele=driver.find_elements(By.XPATH,"//div[@id='navbar-brand-centered']/ul/li")
print(len(ele))
for i in ele:
    print(i.text)
    if i.text=='Selenium':
      i.click()
      print("Selenium is Clicked")






