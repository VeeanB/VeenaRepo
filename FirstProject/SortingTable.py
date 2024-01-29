from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browsersortedveggies =[]
from selenium.webdriver.support.select import Select
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/Offers")
#click on cloumn header to sort
#collect all veggie names --> BrowserSortesveggiesList (B,A,C)
#Sort this BrowserSortesveggiesList --> newSortList -> (A,B,C)
#BrowserSortesveggiesList == new sorted list
driver.find_element(By.CSS_SELECTOR ,".sort-descending").click()
lists = driver.find_elements(By.CSS_SELECTOR ,"tr td:first-child")
print(len(lists))
for list in lists:
    browsersortedveggies.append(list.text)
origionalbrowserSortedList = browsersortedveggies.copy()

browsersortedveggies.sort()
assert  browsersortedveggies == origionalbrowserSortedList

