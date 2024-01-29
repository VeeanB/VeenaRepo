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
driver.get("https://demoqa.com/webtables")
row=len(driver.find_elements(By.XPATH,"//div[@class='rt-table']/div[2]/div"))
col=len(driver.find_elements(By.XPATH,"//div[@class='rt-table']/div[2]/div[1]/div/div"))

print(f"row={row},col={col}")
# for c in range(1,col+1):
#     print(driver.find_element(By.XPATH,f"//div[@class='rt-table']/div[2]/div[1]/div/div[{c}]").text)

# for r in range(1,row+1):
#     print(driver.find_element(By.XPATH,f"//div[@class='rt-table']/div[2]/div[{r}]/div/div[1]").text)

# for r in range(1,row+1):
#     for c in range(1,col+1):
#         print(driver.find_element(By.XPATH,f"//div[@class='rt-table']/div[2]/div[{r}]/div/div[{c}]").text,end="\t")
#     print("\n")

for r in range(1,row+1):
    Name=driver.find_element(By.XPATH,f"//div[@class='rt-table']/div[2]/div[{r}]/div/div[1]").text
    print(Name)
    if 'Kierra' in Name:
        for c in range(1,col+1):
            print(driver.find_element(By.XPATH,f"//div[@class='rt-table']/div[2]/div[{r}]/div/div[{c}]").text)
        break
    #print("\n")