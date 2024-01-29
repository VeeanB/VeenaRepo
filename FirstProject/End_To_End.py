import time

#import ChromeDriverManager as ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.maximize_window()
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://www.google.com")
service_obj = Service(r"C:\Users\veenu\Documents\chromedriver_win32 (2)/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)
driver.maximize_window()
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH ,"//a[text()='Shop']").click()
driver.find_element(By.XPATH ,"//a[text()='iphone X']")
elements =driver.find_elements(By.CSS_SELECTOR ,'.h-100')
print(len(elements))
for element in elements :
    name = element.find_element(By.XPATH ,"div/h4/a").text
    if name == "Blackberry":
        element.find_element(By.XPATH ,"div/button").click()

driver.find_element(By.CSS_SELECTOR ,'.btn-primary').click()
driver.find_element(By.CSS_SELECTOR ,'.btn-success').click()
driver.find_element(By.ID ,'country').send_keys("Ind")
time.sleep(10)
countries = driver.find_elements(By.XPATH ,"//a")
print (len(countries))

for country in countries:
      if country.text == "India":
         country.click()
         break

assert (driver.find_element(By.ID , "country").get_attribute("value")) == "India"

#driver.find_element(By.XPATH ,"//a[text()='term & Conditions']").click()
driver.find_element(By.CSS_SELECTOR ,'.btn-lg').click()
sucess = driver.find_element(By.CSS_SELECTOR,".alert-dismissible").text
assert "Success! Thank you!" in  sucess