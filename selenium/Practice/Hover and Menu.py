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
driver.get("https://www.globalsqa.com/demo-site/tooltip/")
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="post-2679"]/div[2]/div/div/div[1]/p[1]/iframe'))
act= ActionChains(driver)
tooltip= driver.find_element(By.XPATH,"//img[@src='images/st-stephens.jpg']")
act.move_to_element(tooltip).perform()
print(driver.find_element(By.XPATH,"//div[@class='ui-tooltip-content']").text)


sleep(5)
act.move_to_element(driver.find_element(By.XPATH,"/html/body/div[2]/a/img")).perform()
print(driver.find_element(By.XPATH,"//div[@class='ui-tooltip-content']").text)

#************************************************************************************************************************

# driver.get("https://demoqa.com/tool-tips")
# #tool=driver.find_element(By.ID,"toolTipButton")
# #act.move_to_element(tool).perform()
# #print(driver.find_element(By.XPATH,"//div[@class='tooltip-inner']").text)
# text=driver.find_element(By.ID,"texToolTopContainer")
# act.move_to_element(text).perform()
# sleep(5)
# print(driver.find_element(By.XPATH, '//div[@class="tooltip-inner"]').text)

#***************************************************************************************************************************
# driver.get("https://www.bedbathandbeyond.com/")
# menu1=driver.find_element(By.XPATH,"//a[contains(@data-tid,'TN:Bath') and text()='Bath']")
# act.move_to_element(menu1).perform()
# menu2=driver.find_element(By.XPATH,"//a[contains(@data-tid,'TN:Bath:BathroomVanities') and text()='Bathroom Vanities']")
# act.move_to_element(menu2).click().perform()
# print(driver.title)
#***************************************************************************************************************************
# driver.get("https://the-internet.herokuapp.com/hovers")
# tool1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/img")
# act.move_to_element(tool1).perform()
# print(driver.find_element(By.XPATH,"//div/h5[contains(text(),'name: user3')]").text)
#****************************************************************************************************************************
# driver.get("https://artoftesting.com/samplesiteforselenium")
# sleep(5)
# db=driver.find_element(By.ID,"dblClkBtn")
# act.double_click(db).perform()
# alert=driver.switch_to.alert
# sleep(5)
# print(alert.text)
# alert.accept()