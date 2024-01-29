from asyncio import timeout

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

from selenium.webdriver.support.wait import WebDriverWait

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.get("https://demoqa.com/checkbox")
# driver.refresh()
# driver.get("https://demoqa.com/text-box")
# driver.forward()
# driver.back()
#driver.get("https://www.redbus.in")
driver.get("https://www.globalsqa.com/demo-site/accordion-and-tabs/")
print(driver.find_element(By.XPATH,'//h3[@id="ui-id-1"]').is_displayed())
driver.find_element(By.XPATH,'//h3[@id="ui-id-1"]').click()

#time.sleep(20)
driver.maximize_window()
#driver.find_element(By.ID,"cab_rental_vertical").click()
#driver.implicitly_wait(10)
#ob=WebDriverWait(driver,20)
#ob.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"FDHTIaTiPRDb75lTmJwh")))

#print(driver.find_element(By.CLASS_NAME,'FDHTIaTiPRDb75lTmJwh').is_displayed())

#print(ob.until(expected_conditions.alert_is_present(By.CLASS_NAME,"FDHTIaTiPRDb75lTmJwh")))
#print(driver.find_element(By.XPATH,"//img[@class='FDHTIaTiPRDb75lTmJwh']").is_displayed())

#ob1=WebDriverWait(driver,2)
#ob1.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='sIT1HvKpAi1b9I2CBe6s']")))

#print(driver.find_element(By.XPATH,"//div[@class='sIT1HvKpAi1b9I2CBe6s']"))
