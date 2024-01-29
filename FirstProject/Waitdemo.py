from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
