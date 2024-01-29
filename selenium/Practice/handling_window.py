from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import autoit

# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://demoqa.com/browser-windows")
# driver.find_element(By.ID,"tabButton").click()
# print(driver.current_window_handle)
# parent,child=driver.window_handles
# print(child)
# print(parent)
#
# driver.switch_to.window(child)
# driver.close()
# driver.switch_to.window(parent)
# driver.close()
#*****************************************************************************************
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://demoqa.com/browser-windows")
# driver.find_element(By.ID,"tabButton").click()
#
# for i in driver.window_handles[1:]:
#     driver.switch_to.window(i)
#     print(driver.find_element(By.ID,"sampleHeading").text)
#     driver.close()
#******************************************************************************************
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://demoqa.com/browser-windows")
# driver.find_element(By.ID,"windowButton").click()
#
# for i in driver.window_handles[1:]:
#     driver.switch_to.window(i)
#     print(driver.find_element(By.ID,"sampleHeading").text)
#     driver.close
#
#******************************************************************************************
s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.ID,"messageWindowButton").click()
driver.find_element(By.ID,"messageWindowButton").click()

driver.find_element(By.ID,"messageWindowButton").click()
parent,child=driver.window_handles
driver.switch_to.window(child)
driver.close()


