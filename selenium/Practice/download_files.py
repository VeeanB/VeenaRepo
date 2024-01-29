import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


#service_obj=Service("C://chromedriver.exe")
service_obj=Service("c://msedgedriver.exe")
ops=webdriver.EdgeOptions()
#ops= webdriver.ChromeOptions()
preferences={"download.default_directory":location}
ops.add_experimental_option("prefs", preferences)
ops.add_argument("--start-maximized")
ops.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service_obj, options=ops)
ops.add_extension(r"C:\Users\veenu\Downloads\ljngjbnaijcbncmcnjfhigebomdlkcjo.crx")
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.find_element(By.XPATH, "//tbody/tr[1]/td/a[text()='Download sample DOC file']").click()
time.sleep(10)
parent,child = driver.window_handles
driver.switch_to.window(child)
time.sleep(10)
driver.switch_to.frame("wacframe")
driver.find_element(By.XPATH,"//span[text()='Download']").click()
print(len(driver.get_cookies()))
print(driver.get_cookies())
driver.add_cookie({"name":"MyCookies","value":"12345"})
print(len(driver.get_cookies()))
for i in driver.get_cookies():
    print(f"name:{i['name']},value:{i['value']}")



sleep(20)