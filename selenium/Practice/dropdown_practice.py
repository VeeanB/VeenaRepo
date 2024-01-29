from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

sleep(10)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#sleep(10)
wait_ob=WebDriverWait(driver,20)
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='PIM']")))
driver.find_element(By.XPATH,"//span[text()='PIM']").click()
sleep(2)
driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div/div/div/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Hints here for name")
driver.find_element(By.XPATH,"//div[2]/input[@class='oxd-input oxd-input--active']").send_keys("EMP122")
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='oxd-form-row']/div/div[3]/div/div[2]/div/div/div[2]/i")))
driver.find_element(By.XPATH,"//div[@class='oxd-form-row']/div/div[3]/div/div[2]/div/div/div[2]/i").click()
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@role="listbox"]/div/span')))
ele=driver.find_elements(By.XPATH,'//div[@role="listbox"]/div/span')
#try:
for i in ele:
    print(i.text)
    if i.text=="Full-Time Contract":
        i.click()
        print("Clicked Full Time Contract")
        break


#except Exception as msg:
 #   print("Caught as exception")

wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='oxd-form-row']/div/div[4]/div/div[2]/div/div/div[2]/i")))
driver.find_element(By.XPATH,"//div[@class='oxd-form-row']/div/div[4]/div/div[2]/div/div/div[2]/i").click()
sleep(2)
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Current and Past Employees')]").click()
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@id='app']/div/div[2]/div/div/div[1]/div/form/div[1]/div/div[5]/div/div[2]/div/div/input")))
driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div/div/div[1]/div/form/div[1]/div/div[5]/div/div[2]/div/div/input").send_keys("Kevin")
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Kevin')]")))
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Kevin')]").click()
driver.find_element(By.XPATH,"//div[@class='oxd-form-row']/div/div[6]/div/div[2]/div/div/div[2]/i").click()
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Software Engineer')]").click()
driver.find_element(By.XPATH,"//div[@class='oxd-form-row']/div/div[7]/div/div[2]/div/div/div[2]/i").click()
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'OrangeHRM')]")))
#wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='oxd-form-row']/div/div[7]/div/div[2]/div/div[2]/div/span[contains(text(),'OrangeHRm')]")))
driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'OrangeHRM')]").click()
#driver.find_element(By.XPATH,"//div[@class='oxd-form-row']/div/div[7]/div/div[2]/div/div[2]/div/span[contains(text(),'OrangeHRm')]").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(10)
