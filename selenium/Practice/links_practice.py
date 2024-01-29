from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests


service_obj=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
links=driver.find_elements(By.XPATH,"//a")
try:
    for i in links:
        print(i.get_attribute("href"))
        url = i.get_attribute("href")
        scode = requests.get(url)
        print(scode.status_code)
        code = 200
        if scode.status_code>code:
            print(f"Invalid code{input}")
        else:
            print("valid code")
except Exception as msg:
    print("No Status",url,msg)



