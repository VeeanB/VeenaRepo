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
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
#row = len(driver.find_elements(By.XPATH, "//tbody/tr"))
#col = len(driver.find_elements(By.XPATH, "//thead/tr/th"))
#print(f"row:{row} col:{col}")
row= len(driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr"))
col= len(driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[1]/td"))
print(row)
print(col)
for c in range(1,col+1):
   print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr/td[{c}]").text)


# for r in range(1,row+1):
#      print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[1]").text)

# for r in range(1,row+1):
#     for c in range(1,col+1):
#
#         print(driver.find_element(By.XPATH,f"//table[@class='dataTable']/tbody/tr[{r}]/td[{c}]").text,end="\t")
#         print("\n")
#         #print(company)
        #if company =='SAL Steel':
         #   break


# for r in range(1,row+1):
#      company=driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{1}]").text
#      print(company)
#      if 'SAL Steel' in company:
#          for c in range(1, col + 1):
#              print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{c}]").text,end="\t")
#              #print("\n")
#          break
#         #print(driver.find_element(By.XPATH,f"//table[@class='dataTable']/tbody/tr[{r}]/td[{c}]").text,end="\t")
