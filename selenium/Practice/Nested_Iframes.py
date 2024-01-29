from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import autoit
import time
s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://ui.vision/demo/webtest/frames/")
driver.switch_to.frame(driver.find_element(By.XPATH,"//frameset[1]/frameset[1]/frame[1]"))
driver.find_element(By.XPATH,"//form[@id='id2']/div/input").send_keys("Text here1")
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH,"/html[1]/frameset[1]/frame[1]"))
driver.find_element(By.XPATH,"//form[@id='id1']/div/input").send_keys("Text here2")
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/frameset/frameset/frame[2]"))
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/center/iframe"))
time.sleep(10)
driver.find_element(By.XPATH,"/html[1]/body[1]/center[1]/iframe[1]").click()
