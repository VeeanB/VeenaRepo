# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/")
# sleep(10)
# driver.find_element(By.XPATH,"//a[contains(text(),'JavaScript Alerts')]").click()
# # driver.find_element(By.XPATH,"//li/button[contains(text(),'Click for JS Alert')]").click()
# # alert=driver.switch_to.alert
# # alert.accept()
# #driver.find_element(By.XPATH,"//li/button[contains(text(),'Click for JS Confirm')]").click()
# #alert=driver.switch_to.alert
# #alert.accept()
# #alert.dismiss()
# #print(driver.find_element(By.XPATH,"//p[@id='result']").text)
#
# driver.find_element(By.XPATH,"//li/button[contains(text(),'Click for JS Prompt')]").click()
# alert=driver.switch_to.alert
# #alert.send_keys("Veena")
# #alert.accept()
# alert.dismiss()
# print(driver.find_element(By.XPATH,"//p[@id='result']").text)
#*********************************************************************************************************
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://www.globalsqa.com/samplepagetest/")
# sleep(10)
# driver.find_element(By.XPATH,"//button[contains(text(),'Alert Box : Click Here')]").click()
# alert=driver.switch_to.alert
# alert.accept()
# sleep(10)
# alert.accept()

#*************************************************************************************************************
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# import autoit
#
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# #driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# autoit.win_wait_active("",30)
# autoit.send("admin{TAB}")
# autoit.send("admin{ENTER}")
# sleep(10)
# #driver.find_element(By.XPATH,"//a[contains(text(),'Basic Auth')]")

#**************************************************************************************************************
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# import autoit
#
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://demoqa.com/alerts")
# #driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
# #driver.find_element(By.XPATH,"//button[@id='timerAlertButton']").click()
# sleep(5)
# #driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
#
# driver.find_element(By.XPATH,"//button[@id='promtButton']").click()
# alert=driver.switch_to.alert
# #alert.accept()
# #alert.dismiss()
# alert.send_keys("Veena")
# alert.dismiss()
# #print(driver.find_element(By.XPATH,"//span[@id='confirmResult']").text)
# #print(driver.find_element(By.XPATH,"//span[@id='promptResult']").text)
# sleep(10)

#****************************************************************************************

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import autoit

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://artoftesting.com/samplesiteforselenium")
sleep(5)
#driver.find_element(By.XPATH,"//button[contains(text(),'Generate Alert Box')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Generate Confirm Box')]").click()
alert=driver.switch_to.alert
#alert.accept()

print(alert.text)
alert.dismiss()
print(driver.find_element(By.XPATH,"//p[@id='demo']").text)

