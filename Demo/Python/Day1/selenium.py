from  time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service("C:chromedriver.exe")
#service_obj=Service()# no path --> fetch from web---> slow-->securirty breaches-->mismatch of verison
driver = webdriver.Chrome(service=service_obj)

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
sleep(5)
driver.close()
