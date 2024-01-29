from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)
driver.maximize_window()
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT ,'Click Here').click()
windownsOpened = driver.window_handles
driver.switch_to.window(windownsOpened[1])
print(driver.find_element(By.TAG_NAME ,"h3").text)
driver.switch_to.window(windownsOpened[0])
print(driver.find_element(By.TAG_NAME ,"h3").text)


