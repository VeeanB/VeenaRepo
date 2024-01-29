from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome
name = "Rahul"
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID ,'name').send_keys(name)
driver.find_element(By.ID , 'alertbtn').click()
alert = driver.switch_to.alert
alerttext =alert.text
print(alerttext)
assert name in alerttext
alert.accept()
#alert.dismiss()
