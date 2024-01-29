from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.save70.com/flights/?campaignid=16568085087&adgroupid=134041419349&lpage=k&lb=skys&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh00P-oj6XQ3qdYZTmmPmlGVdGjLvhnUodahSf3BxOci0MY4bslIzKAaAsJSEALw_wcB")
#sleep(10)
driver.find_element(By.ID,"flights_depart_date").click()
month='June'
# sleep(10)
# while True:
#     month_list=[]
#     for i in driver.find_elements(By.XPATH, f"//span[@class='ui-datepicker-month']"):
#         month_list.append(i.text)# collect both month from the container
#
#     if month == month_list[0]:#comparing first grp month()
#         break
#     else:
#         driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/div/a/span").click()
#
# driver.find_element(By.XPATH, "//div[@class='ui-datepicker-group ui-datepicker-group-first']/table/tbody/tr/td/a[text()='30']").click()
#selecting first group data
while True:
 li=[]
 months = driver.find_elements(By.XPATH, "//span[@class='ui-datepicker-month']")
 for i in months:
     li.append(i.text)
 if month in li:
     break
 else:
    driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/div/a/span").click()
dates=driver.find_elements(By.XPATH,"//div[@class='ui-datepicker-group ui-datepicker-group-last']/table/tbody/tr/td")
for i in dates:
    if i.text=='21':
        i.click()
        break

print(driver.find_element(By.ID,"flights_depart_date").get_attribute("value"))