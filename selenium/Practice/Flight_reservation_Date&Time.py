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
driver.get("https://www.save70.com/flights/?campaignid=16568085087&adgroupid=134041419349&lpage=k&lb=skys&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh00P-oj6XQ3qdYZTmmPmlGVdGjLvhnUodahSf3BxOci0MY4bslIzKAaAsJSEALw_wcB")
driver.maximize_window()
driver.find_element(By.ID,"flights_depart_date").click()
eles=driver.find_elements(By.XPATH,"//div[@class='ui-datepicker-title']")
month="March"
for i in eles:
    if i.text==month:
        i.click()
    elif i.text!=month:
        driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']").click()
        dates=driver.find_elements(By.XPATH,"//a[@class='ui-state-default']")
        for i in dates:
            if i.text=="31":
                i.click()
                break

    break

#driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']").click()
# dates=driver.find_elements(By.XPATH,"/html/body/div[15]/div[1]/table/tbody/tr/td/a")
# for i in dates:
#     if i.text=="31":
#         i.click()
#         break
tme=Select(driver.find_element(By.ID,"flights_departure_time"))
tme.select_by_visible_text("10:00 AM")
time.sleep(5)
#****************************************************************************************************
# driver.get("https://www.globalsqa.com/demo-site/datepicker/")
# driver.find_element(By.ID,"Icon Trigger").click()
# time.sleep(5)
# driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[3]/p/iframe"))
# driver.find_element(By.XPATH,"//img[@class='ui-datepicker-trigger']").click()
# driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
# days=driver.find_elements(By.XPATH,"//tr/td/a")
# for i in days:
#     if i.text=="31":
#         i.click()
#         break
#
# time.sleep(5)