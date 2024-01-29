from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://money.rediff.com/gainers")

#print(driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/table/tbody/tr[12]/td[4]").text)

#//table[@class='dataTable']/tbody/tr[2]/child::td
#//table[@class='dataTable']/tbody/tr[2]/td/self::td
#//div[contains(text(),'Weekly')]/following-sibling::div
#//div[@class='tabs'][2]/following-sibling::div
#//div[@class='tabs'][2]/ancestor::div
#//div[@class='tabs'][2]/preceding::div
#//a[contains(text(),'Weekly')]/parent::div
#//*[contains(text(),'Weekly')]/ancestor::div
#//*[contains(text(),'Weekly')]/parent::div
#//a[contains(text(),'Weekly')]/self::a Or //*[contains(text(),'Weekly')]/self::a
#//a[contains(text(),'Investment Tool')]/following::li

#//table[@class='dataTable']/tbody/tr/td/parent::tr
#//table[@class='dataTable']/tbody/tr/td/following::tr
#//table[@class='dataTable']/tbody/tr/child::td
#//table[@class='dataTable']/tbody/tr/td/self::td
#//table[@class='dataTable']/tbody/tr/preceding::td
#//table[@class='dataTable']/tbody/tr/td/following-sibling::td
#//table[@class='dataTable']/tbody/tr/td/preceding-sibling::td
#//table[@class='dataTable']/tbody/tr/descendant::td
#//table[@class='dataTable']/tbody/tr/td/ancestor::tr


#//table[@class='dataTable']/tbody/tr[8]/td[3]
# //a[contains(text(),'Goblin India')]/ancestor::tr/td[3]/preceding-sibling::td
# //a[contains(text(),'Goblin India')]/ancestor::tr/td[3]/following-sibling::td
# //a[contains(text(),'Goblin India')]/ancestor::tr/td[3]/preceding::td
# //a[contains(text(),'Goblin India')]/ancestor::tr/td[3]/following::td