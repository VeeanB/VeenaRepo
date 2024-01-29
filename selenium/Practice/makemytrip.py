# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# import time
#
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://www.makemytrip.com/")
# time.sleep(20)
#
# driver.find_element(By.XPATH,"//input[@id='fromCity']").send_keys("BLR")
# source=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li")
# print(len(source))
# for i in source:
#     print(i.text)
#     if 'Bengaluru, India' in i.text:
#         i.click()
#         print("Selected Bengaluru, India")
#         break
#
# driver.find_element(By.XPATH,"//div[@data-cy='flightTraveller']/label/span[text()='Travellers & Class']").click()
# driver.find_element(By.XPATH,"//ul[@class='guestCounter font12 darkText gbCounter']/li[text()='4']").click()
# driver.find_element(By.XPATH,"//ul[@class='guestCounter classSelect font12 darkText']/li[text()='Premium Economy']").click()
# driver.find_element(By.XPATH,'//button[@class="primaryBtn btnApply pushRight"]').click()
# time.sleep(10)
#*************************************************************

# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# import time
#
# s=Service("C://chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://www.amazon.com/")
# #time.sleep(10)
# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Gift")
# time.sleep(10)
# ele=driver.find_elements(By.XPATH,"//div[@class='s-suggestion-container']/div")
# print(len(ele))
# for i in ele:
#     print(i.text)
#     if i.text=='gifts for women':
#         i.click()
#         print("Selected gifts for women")

#***********************************************************************

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/auto-complete/#Categories")
#time.sleep(10)
# wait_obj=WebDriverWait(driver, 20)
# wait_obj.WebDriverWait.until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@id="search"]')))
# print(wait_obj)
# print(driver.find_element(By.XPATH,'//input[@id="search"]').is_displayed())
driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='twelve columns']/div/div/div[1]/p/iframe"))
driver.find_element(By.XPATH,'//input[@id="search"]').send_keys("A")
ele=driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li/div")
print(len(ele))
for i in ele:
    print(i.text)


