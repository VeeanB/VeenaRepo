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
#driver.get("https://cosmocode.io/automation-practice-webtable/")

#row = len(driver.find_elements(By.XPATH,"//table[@id='countries']/tbody/tr"))
#col = len(driver.find_elements(By.XPATH,"//table[@id='countries']/tbody/tr[1]/td"))
#print(f"row ={row}, col={col}")
#for c in range(1,col+1):
 #   print(driver.find_element(By.XPATH,f"//table[@id='countries']/tbody/tr/td[{c}]").text) #only heading is displaying

# for r in range(1,row+1):
#     print(driver.find_element(By.XPATH,f"//table[@id='countries']/tbody/tr[{r}]/td[2]").text)

# for r in range(1,row+1):
#     cntry=driver.find_element(By.XPATH,f"//table[@id='countries']/tbody/tr[{r}]/td[{2}]").text
#     print(cntry)
#     if 'Andorra' in cntry:
#         for c in range(1,col+1):
#             print(driver.find_element(By.XPATH,f"//table[@id='countries']/tbody/tr[{r}]/td[{c}]").text,end="\t")
#         break
        #print("\n")
#*********************************************************************************************************
driver.get("https://www.dezlearn.com/webtable-example/")
row = len(driver.find_elements(By.XPATH,"//table[@class='tg']/tbody/tr"))
col = len(driver.find_elements(By.XPATH,"//table[@class='tg']/tbody/tr[2]/td"))
print(f"row={row}, col={col}")
#for c in range(1,col+1):
 #   print(driver.find_element(By.XPATH,f"//table[@class='tg']/tbody/tr/td[{c}]").text)
# for r in range(2,row+1):
#     print(driver.find_element(By.XPATH,f"//table[@class='tg']/tbody/tr[{r}]/td[1]").text)

# for r in range(2,row+1):
#     for c in range(1,col+1):
#         print(driver.find_element(By.XPATH,f"//table[@class='tg']/tbody/tr[{r}]/td[{c}]").text,end="\t")
#         print("\n")
for r in range(2,row+1):
    Name=driver.find_element(By.XPATH,f"//table[@class='tg']/tbody/tr[{r}]/td[1]").text
    print(Name)
    if Name =='John White':
        for c in range(1,col+1):
            print(driver.find_element(By.XPATH,f"//table[@class='tg']/tbody/tr[{r}]/td[{c}]").text)
        break

