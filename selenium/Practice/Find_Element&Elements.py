from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://money.rediff.com/gainers/nse")
driver.maximize_window()
driver.implicitly_wait(10)
# driver.find_element(By.NAME,"username").send_keys("Admin")
# print(driver.find_element(By.NAME,"username").get_property('value'))
# driver.find_element(By.NAME,"username").clear()
# driver.find_element(By.NAME,"username").send_keys("Admin123")
# print(driver.find_element(By.NAME,"username").get_property('value'))
#driver.find_element(By.NAME,"username").send_keys("Admin")
#driver.find_element(By.NAME,"password").send_keys("admin123")
#ele=driver.find_elements(By.XPATH,'//a[contains(text(),"Orchid Pharma")]/parent::td/following::tr')
# print(ele.text)
#elems=driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/following::td")
# print(elems)
#for i in ele:
 #   print(i.text)
# driver.close()
ele=driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[8]/td")
print(len(ele))
for i in ele:
    print(i.text)
    if i.text=='HUDCO':
        i.click()
        print("HUDCO clicked")

