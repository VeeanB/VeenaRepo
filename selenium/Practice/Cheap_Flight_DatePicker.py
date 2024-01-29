import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
def random_emailgen():
  email_gen = ""
  for i in range(8):

   email_gen=email_gen+random.choice(string.ascii_letters+string.digits)
  return email_gen


s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.save70.com/flights/?campaignid=16568085087&adgroupid=134041419349&lpage=k&lb=skys&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh00P-oj6XQ3qdYZTmmPmlGVdGjLvhnUodahSf3BxOci0MY4bslIzKAaAsJSEALw_wcB")
driver.find_element(By.ID,"flights_depart_date").click()
#pre=driver.find_element(By.XPATH,"//a/span[@class='ui-icon ui-icon-circle-triangle-w']").is_displayed()
#nex=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
month='July'
while True:
    month_list = []
    months=driver.find_elements(By.XPATH, f"//span[@class='ui-datepicker-month']")
    for i in months:
        month_list.append(i.text)
    if month in month_list:
     break
    else:
          driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/div/a/span").click()
    #break

#driver.find_element(By.XPATH, "//div[@class='ui-datepicker-group ui-datepicker-group-first']/table/tbody/tr/td/a[text()='30']").click()

print("outside of loop")

dates=driver.find_elements(By.XPATH,"//div[@class='ui-datepicker-group ui-datepicker-group-last']/table/tbody/tr/td")
for i in dates:
    if i.text=='31':
        i.click()
        break

sleep(5)
#break
print(driver.find_element(By.ID,"flights_depart_date").get_attribute("value"))

print(random_emailgen()+f"@gmail.com")
