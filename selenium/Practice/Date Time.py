from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
import time
from selenium.webdriver.support.ui import Select
import datetime

Service_obj=Service("C://chromedriver.exe")
#Service_obj=Service("C://geckodriver.exe")
# ops=webdriver.ChromeOptions()
# ops=webdriver.FirefoxOptions()
# ops.add_argument("--start-maximized")
# ops.add_argument("--incognito")
#ops.add_argument("headless")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://demoqa.com/date-picker")
driver.maximize_window()
# print(datetime.datetime.now())
# current_time=datetime.datetime.now()
# print(current_time.strftime("%Y-%m-%d %H:%M:%S.%ms,%p"))
# spec_time=datetime.datetime(2023,12,29, 12,49,57)
# print(spec_time.strftime("%m %d, %Y %H:%M:%S:%f %p"))
# year=spec_time.strftime("%Y")
# date=spec_time.strftime("%d").lstrip("0")
# month=spec_time.strftime("%m")
# hour=spec_time.strftime("%H").lstrip("0")
# sec=spec_time.strftime("%S")
# time_eq=spec_time.strftime("%p")
# print(f"{year}-{date}-{month} {hour}:{sec}:{time_eq}")
day="25"
driver.find_element(By.ID,"datePickerMonthYearInput").click()
yr=Select(driver.find_element(By.XPATH,"//*[@id='datePickerMonthYear']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select"))
yr.select_by_visible_text("2025")
date=Select(driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select"))
date.select_by_visible_text("May")
driver.find_element(By.XPATH,f'//div[contains(@class, "react-datepicker__day react-datepicker__day--0{day}") and not (contains(@class,"react-datepicker__day react-datepicker__day--0{day} react-datepicker__day--outside-month"))]').click()
time.sleep(5)
driver.find_element(By.ID,"dateAndTimePickerInput").click()
driver.find_element(By.XPATH,"//div[@class='react-datepicker__year-read-view']").click()
years=driver.find_elements(By.XPATH,"//div[(@class='react-datepicker__year-option') or (@class='react-datepicker__year-option react-datepicker__year-option--selected_year')]")
year="2025"
for i in years:
    if year in i.text:
        i.click()
        break

driver.find_element(By.XPATH,"//*[@id='dateAndTimePicker']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/span[1]").click()
months=driver.find_elements(By.XPATH,"//div[(@class='react-datepicker__month-option') or (@class='react-datepicker__month-option react-datepicker__month-option--selected_month')]")
for i in months:
    if i.text=='May':
        i.click()
        break
driver.find_element(By.XPATH,"//div[contains(@class,'react-datepicker__day react-datepicker__day--025') and not (contains(@class,'react-datepicker__day react-datepicker__day--026 react-datepicker__day--weekend react-datepicker__day--outside-month'))]").click()

time=driver.find_elements(By.XPATH,"//ul/li[@class='react-datepicker__time-list-item ']")
for i in time:
    if i.text=='13:15':
        i.click()
        break


print(driver.find_element(By.ID,"dateAndTimePickerInput").get_attribute("value"))
