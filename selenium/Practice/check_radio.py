from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

from selenium.webdriver.support.wait import WebDriverWait

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://demoqa.com/radio-button")
#driver.find_element(By.XPATH,"//span[@class='rct-checkbox']/*[name()='svg']").click()
#print(driver.find_element(By.XPATH,"//span[@class='rct-checkbox']/*[name()='svg']").is_selected())
#print(driver.find_element(By.XPATH,'//input[@id="tree-node-home"]').is_selected())
#print(driver.find_element(By.XPATH,'//div[@id="result"]').text)
#driver.find_element(By.XPATH,"//button[@class='rct-collapse rct-collapse-btn']").click()
#driver.find_element(By.XPATH,"//input[@id='tree-node-downloads']/following-sibling::span[@class='rct-checkbox']/*[name()='svg']").click()
#time.sleep(20)
print(driver.find_element(By.XPATH,"//input[@id='noRadio']/following-sibling::label").is_enabled())
#print(driver.find_element(By.XPATH,"//p[@class='mt-3']").text)