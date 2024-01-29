from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://www.zimyo.work/")
driver.find_element(By.NAME ,'username').send_keys("9880444819")
driver.find_element(By.NAME ,'password').send_keys("Veena@123")
driver.find_element(By.XPATH ,"//button[@class='MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-disableElevation MuiButtonBase-root w-100 css-1e5kyoo-MuiButtonBase-root-MuiButton-root']").click()
driver.find_element(By.XPATH ,"//h6[text()='Clock Out']").click()

