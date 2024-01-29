from time import sleep

import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from xlutility_Practice import *

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
test_data=r"C:\Users\veenu\Downloads\Simple_Interest.xlsx"
#wb=openpyxl.load_workbook(test_data)
#Sheet=wb["Sheet1"]
for r in range(2, getRow(test_data, "Sheet1")+1):
    Int_Type=getValue(test_data,"Sheet1",r,1)
    Principle=getValue(test_data,"Sheet1",r,2)
    Rate=getValue(test_data,"Sheet1",r,3)
    Period_Unit=getValue(test_data,"Sheet1",r,4)
    Period_Opt=getValue(test_data,"Sheet1",r,5)
# Interest_drp=Select(driver.find_element(By.ID,"a"))
# Interest_drp.select_by_visible_text(Int_Type)
# driver.find_element(By.ID,"c").clear()
# driver.find_element(By.ID,"c").send_keys(Principle)
# driver.find_element(By.ID,"d").clear()
# driver.find_element(By.ID,"d").send_keys(Rate)
# driver.find_element(By.ID,"e").clear()
# driver.find_element(By.ID,"e").send_keys(Period_Unit)
# Period_drp=Select(driver.find_element(By.ID,"f"))
# Period_drp.select_by_visible_text(Period_Unit)
# driver.find_element(By.ID,"e").send_keys(Period_Opt)
# print(driver.find_element(By.XPATH,"//label[text()='Total Value']/following-sibling::span").text)
    Interest_drp=Select(driver.find_element(By.ID,"a"))
    Interest_drp.select_by_visible_text(Int_Type)
    driver.find_element(By.ID,"c").clear()
    driver.find_element(By.ID,"c").send_keys(Principle)
    driver.find_element(By.ID,"d").clear()
    driver.find_element(By.ID,"d").send_keys(Rate)
    driver.find_element(By.ID,"e").clear()
    driver.find_element(By.ID,"e").send_keys(Period_Opt)
    Period_drp=Select(driver.find_element(By.ID,"f"))
    Period_drp.select_by_visible_text(Period_Unit)
    total=driver.find_element(By.XPATH,"//label[text()='Total Value']/following-sibling::span").text
    print(total)
    writeValue(test_data,"Sheet1",r,8,total)
    print(float(total.strip("₹ ").replace(",","")))
    excel_total_value = getValue(test_data, "Sheet1", r, 6)
  #  print(float(excel_total_value))
    if float(total.strip("₹ ").replace(",", "")) == float(excel_total_value):
        writeValue(test_data,"Sheet1",r,9,"Pass")
        fillGreen(test_data,"Sheet1",r,9)
        fillGreen(test_data,"Sheet1",r,7)
        fillGreen(test_data, "Sheet1", r, 8)
      #  print(True)
    else:
        writeValue(test_data, "Sheet1", r, 9, "Fail")
        fillRed(test_data,"Sheet1",r,9)
        fillRed(test_data, "Sheet1", r, 7)
        fillRed(test_data, "Sheet1", r, 8)
       # print(False)
sleep(5)