from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj=Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demoqa.com/date-picker")
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
Min=spec_time.strftime("%M")
time_eq=spec_time.strftime("%p")
print(f"{month} {date}, {year} {hour_12format}:{Min} {time_eq}")
#################not working
# driver.find_element(By.ID, "dateAndTimePickerInput").click()
# driver.find_element(By.ID, "dateAndTimePickerInput").clear()
# driver.find_element(By.ID, "dateAndTimePickerInput").send_keys(f"{month} {date}, {year} {hour}:{sec} {time_eq}")
# sleep(15)
#######################################3
# # order to select # year month date hour min sec millisec
#
driver.find_element(By.ID, "dateAndTimePickerInput").click()
# years
driver.find_element(By.XPATH, "//div[@class='react-datepicker__year-read-view']").click()


while True:
    yrs_elm = driver.find_elements(By.XPATH, "//div[contains(@class,'react-datepicker__year-option')]")# webelem
    years_list = []
    for i in yrs_elm:
        if i.text!="":
            years_list.append(i.text.strip("✓\n")) # year text
    #current container[2019,2018,...1999]
    if int(years_list[-1])>int(year):
        driver.find_element(By.XPATH, '//div[contains(@class,"react-datepicker__year-option")]/a[contains(@class, "years-previous")]').click()
    elif int(years_list[0])<int(year):
        driver.find_element(By.XPATH, '//div[contains(@class,"react-datepicker__year-option")]/a[contains(@class, "years-upcoming")]').click()
    elif year in years_list:
        for i in yrs_elm:
            if year in i.text:
                i.click()
                break
        break



# month
# driver.find_element(By.XPATH, "//div[@class='react-datepicker__month-read-view']").click()
# mon_elm = driver.find_elements(By.XPATH, "//div[contains(@class,'react-datepicker__month-option')]")
# for i in mon_elm:
#     print(i.text)
#     if i.text.strip("✓\n")==month:
#         i.click()
#         break


# day
day=spec_time.strftime("%d")
print(f'//div[contains(@class, "react-datepicker__day react-datepicker__day--0{day}") and not (contains(@class,"react-datepicker__day--outside-month"))]')
driver.find_element(By.XPATH,f'//div[contains(@class, "react-datepicker__day react-datepicker__day--0{day}") and not (contains(@class,"react-datepicker__day--outside-month"))]').click()



# time

time=driver.find_elements(By.XPATH,"//ul/li[@class='react-datepicker__time-list-item ']")
for i in time:
    if i.text==f'{hour_24format}:{Min}':
        i.click()
        break


ele=driver.find_element(By.XPATH,"//body").click()
Act=ActionChains(driver)
Act.send_keys(Keys.TAB)
actual_date = driver.find_element(By.ID,"dateAndTimePickerInput").get_attribute("value")
print("actual date", actual_date)
print(f"format date: {month} {date}, {year} {hour_12format}:{Min} {time_eq}")
if actual_date == f"{month} {date}, {year} {hour_12format}:{Min} {time_eq}":
    assert True
else:
    assert False, "date format is wrong"



#react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-previous
#react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-upcoming


# //div[contains(@class,'react-datepicker__year-option')]/a[contains(@class, "years-previous")]
#react-datepicker__month-option react-datepicker__month-option--selected_month
# //div[@class='react-datepicker__month-option']