from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support.ui import Select


service_obj=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

sleep(10)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.maximize_window()
# CDT= datetime.datetime(2035, 8, 23,2, 45)#datetime.datetime.now()
# print(CDT)
# year=CDT.strftime("%Y")
# month=CDT.strftime("%m")
# date=CDT.strftime("%d")
# hour=CDT.strftime("%H")
# min=CDT.strftime("%M")
# second=CDT.strftime("%S")
# eq_value=CDT.strftime("%p")
# print(f"{year}-{month}-{date} {hour}:{min}:{second} {eq_value}")
# driver.find_element(By.ID,"datePickerMonthYearInput").click()
# year_drp=Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']"))
# year_drp.select_by_visible_text("1990")
# sleep(5)
# driver.find_element(By.ID,"dateAndTimePickerInput").click()
# driver.find_element(By.XPATH,"//div[@class='react-datepicker__year-read-view']").click()
#
# while True:

#     year_ele=driver.find_elements(By.XPATH,"//div[contains(@class,'react-datepicker__year-option')]")
#     year_list=[]
#     for i in year_ele:
#         if i.text!="":
#             year_list.append(i.text.strip("✓\n"))
#     if int(year_list[-1])>int(year):
#         driver.find_element(By.XPATH,"//a[@class='react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-previous']").click()
#     elif int(year_list[0])<int(year):
#         driver.find_element(By.XPATH,"//a[@class='react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-upcoming']").click()
#     elif year in year_ele:
#         for i in year_ele:
#             if year in i.text:
#                 i.click()
#                 break
#     break
# print(year)
# print(CDT)
# if year==CDT:
#     assert True
# else:
#     assert False,"Not Matching"

driver.find_element(By.XPATH,"//li/a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").click()

