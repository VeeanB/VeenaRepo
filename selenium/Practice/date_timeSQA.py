from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

service_obj=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.globalsqa.com/demo-site/datepicker/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"DropDown DatePicker").click()
driver.maximize_window()


#############################################################
# December 9, 2023 3:04 AM
# spec_time=datetime.datetime(2035, 8, 23,2, 45)
spec_time=datetime.datetime.now() #current date and time

year=spec_time.strftime("%Y")
date=spec_time.strftime("%d").lstrip("0")
month=spec_time.strftime("%B")
hour_24format=spec_time.strftime("%H")
hour_12format=spec_time.strftime("%I").lstrip("0")
sec=spec_time.strftime("%S")
time_eq=spec_time.strftime("%p")
print(f"{month} {date}, {year} {hour_12format}:{sec} {time_eq}")
driver.implicitly_wait(5)
driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='post-2661']/div[2]/div/div/div[2]/p/iframe"))
driver.find_element(By.ID,"datepicker").click()
drop=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
drop.select_by_visible_text("2034")
sleep(5)