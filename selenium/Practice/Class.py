from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
print(driver.title)
elems=driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/following::td")
for i in elems:
    print(i.text)
sleep(1)
driver.close()