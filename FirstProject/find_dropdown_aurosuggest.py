import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.webdriver.firefox.service import Service
#Edge
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID , "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR ,"li[class='ui-menu-item'] a")
print (len(countries))

for country in countries:
      if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID , "autosuggest").text) it wont work for dynamic
#print(driver.find_element(By.ID , "autosuggest").get_attribute("value"))
assert (driver.find_element(By.ID , "autosuggest").get_attribute("value")) == "India"

