from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import autoit

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demoqa.com/nestedframes")

# print(driver.find_element(By.XPATH,"//div[@id='framesWrapper']/div").text)
# driver.switch_to.frame("frame1")
# print(driver.find_element(By.ID,"sampleHeading").text)
# driver.switch_to.default_content()
# print(driver.find_element(By.XPATH,"//div[@id='framesWrapper']/div").text)
#*********************************************************************************
# print(driver.find_element(By.XPATH,"//div[@id='framesWrapper']/div").text)
# driver.switch_to.frame("frame2")
# print(driver.find_element(By.XPATH,"//h1[@id='sampleHeading']").text)
# driver.switch_to.default_content()
# print(driver.find_element(By.XPATH,"//div[@id='framesWrapper']/div").text)
# driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@id='frame1Wrapper']/iframe"))
# print(driver.find_element(By.ID,"sampleHeading").text)
#***********************************************************************************
print(driver.find_element(By.XPATH,"//div[@id='framesWrapper']/div").text)
driver.switch_to.frame("frame1")
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@srcdoc="<p>Child Iframe</p>"]'))
print(driver.find_element(By.XPATH,"//body/p").text)
driver.switch_to.parent_frame()
print(driver.find_element(By.XPATH,"//body").text)
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//div[@id='framesWrapper']/div").text)


