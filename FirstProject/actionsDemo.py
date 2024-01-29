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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.double_click(driver.find_element(By.ID ,"mousehover"))
#action.click(driver.find_element(By.ID ,"mousehover"))
#action.drag_and_drop()
#action.context_click()
action.move_to_element(driver.find_element(By.ID ,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT ,"Top")).perform()
#action.click_and_hold("")
action.move_to_element(driver.find_element(By.ID ,"Reload")).click().perform()