from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import autoit
from selenium.webdriver import ActionChains
s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
act=ActionChains(driver)
sleep(5)
source=driver.find_element(By.XPATH,"//div[@id='column-a']")
destination=driver.find_element(By.XPATH,"//div[@id='column-b']")
act.drag_and_drop(source,destination).perform()
sleep(10)
