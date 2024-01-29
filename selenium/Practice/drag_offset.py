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
#driver.get("https://demoqa.com/dragabble")
#ele=driver.find_element(By.ID,"dragBox")
act=ActionChains(driver)
#print(ele.location)
#act.drag_and_drop_by_offset(ele,400,400).perform()
#act.scroll_to_element(ele).perform()

#driver.execute_script("arguments[0].scrollIntoView()",ele)
#act.scroll_by_amount(-100,-100).perform()
#act.scroll_to_element(ele)
#print(ele.location)
#sleep(10)
#*******************************************************************************************************************************
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(3)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#sleep(10)
wait_ob=WebDriverWait(driver,20)
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='PIM']")))
driver.find_element(By.XPATH,"//span[text()='PIM']").click()
sleep(5)
ele=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i').click()
elem = driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Software Engineer')]")
#act.scroll_to_element(elem).perform()
driver.execute_script("arguments[0].scrollIntoView()",driver.find_element(By.XPATH,"//div[text()='QA Lead']"))
sleep(5)