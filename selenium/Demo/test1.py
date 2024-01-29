from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/geckodriver.exe")
#s=Service("C:\\chromedriver.exe")
#s=Service("C:/msedgedriver.exe")

#browser = webdriver.Chrome(service=s)
browser = webdriver.Firefox(service=s)
#browser = webdriver.Edge(service=s)
browser.get("https://www.google.com")
browser.maximize_window()

#browser.get("https://www.geeksforgeeks.org/")
#browser.find_element(By.PARTIAL_LINK_TEXT, "Sign").click()
#browser.get("https://opensource-demo.orangehrmlive.com/web/index.php")
#browser.implicitly_wait(2)
#browser.find_element(By.NAME,"username").send_keys("Admin")
#browser.find_element(By.NAME,"password").send_keys("admin123")
#browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#browser.find_element(By.PARTIAL_LINK_TEXT,"Admin").click()
#browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("New Role")
#browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div').click()
#browser.find_element(By.XPATH,"").is_selected()

