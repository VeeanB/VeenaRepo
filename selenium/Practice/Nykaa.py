from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import autoit

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.nykaafashion.com/women/indianwear/kurtis-kurtas-and-tunics/c/662?transaction_id=6b031f377129d95635116cb3ce6d547e&intcmp=nykaa:other:nf-indianwear:default:top-categories:SLIDING_WIDGET_V2:1:kurtas:-1:6b031f377129d95635116cb3ce6d547e")
list= driver.find_elements(By.XPATH,"//div[@class='css-nkwpjp']/div[2]")
print(len(list))
for i in list:
    if i.text=='Likha':
     print(i.find_element(By.XPATH, "//div[@class='css-nkwpjp']/div[5]/span[1]").text)
     i.click()
     sleep(10)
     break


