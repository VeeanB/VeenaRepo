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
driver.get("https://www.save70.com/flights/?campaignid=16568085087&adgroupid=134041419349&lpage=k&lb=skys&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh00P-oj6XQ3qdYZTmmPmlGVdGjLvhnUodahSf3BxOci0MY4bslIzKAaAsJSEALw_wcB")#
driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").send_keys("AL")
#driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").send_keys(Keys.ENTER)
time.sleep(10)
ele=driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li[@class='ui-menu-item']")
print(len(ele))
time.sleep(5)
for i in ele:
    print(i.text)
    if i.text=='Albuquerque, United States - Albuquerque International Sunport (ABQ)':
        i.click()


driver.find_element(By.XPATH,"//input[@placeholder='Destination name or code']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Destination name or code']").send_keys("T")
time.sleep(5)
#ob=WebDriverWait.until(expected_conditions((By.XPATH,"//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all tbjs-autocomplete-ul']/li")))
ele1=driver.find_elements(By.XPATH,"//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all tbjs-autocomplete-ul']/li")

print(len(ele1))
for j in ele1:
    print(j.text)
    if j.text=='Houston, United States - Hobby & All airports (HOU)':
        j.click()
        print("Selected Houston, United States - Hobby & All airports (HOU)")


#print(driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").text)
#drop = Select(driver.find_element(By.XPATH,"//select[@name='flights_class']"))
#drop.select_by_visible_text("First")
#print(driver.find_element(By.XPATH,"//select[@name='flights_class']").text)



#here from field is not displayin the lists
