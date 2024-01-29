import string
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://thread-v2.platform.threadresearch.com/#/login")
N=5
driver.maximize_window()
driver.find_element(By.ID ,'username').send_keys("veena.badalakkanavar@aventior.com")
driver.find_element(By.ID ,'password').send_keys("Test#1234")
driver.find_element(By.XPATH ,'//button[@type ="submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[contains(text(),'Activity Library')]").click()
driver.find_element(By.CLASS_NAME ,'text').click()
dropdown =(Select(driver.find_element(By.NAME, 'activityType')))
dropdown.select_by_visible_text("ClinRO")
letters = string.ascii_lowercase
name =print('AC'.join(random.choices(string.ascii_lowercase,k = N)))
driver.find_element(By.NAME ,'title').send_keys(name)

#print ( ''.join(random.choice(letters) for i in range(10)) )
