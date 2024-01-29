from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
#Edge
service_obj = Service("/Users/veenu/Documents/edgedriver_win64/msedgedriver")
driver = webdriver.Edge(service=service_obj)
#Firefox
#service_obj = Service("/geckodriver")
#driver = webdriver.Firefox(service=service_obj)
#chrome driver
#service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
#driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
a = driver.title
print(a)
print(driver.current_url)
#driver.minimize_window()
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.refresh()
driver.forward()
driver.close()
