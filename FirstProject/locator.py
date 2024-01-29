from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")

#from selenium.webdriver.firefox.service import Service
#Edge
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj , options=chrome_option)

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR , "input[name='name']").send_keys("Veena")
driver.find_element(By.NAME, "email").send_keys("veenumb@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
#driver.find_element((By.XPATH, "//input[@id = 'exampleCheck1']")).click()
dropdown = Select(driver.find_element(By.ID ,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)#Male is selected

# //tagename[@attribute ='Submit'] , #id,   .Classname,
driver.find_element(By.XPATH , "//input[@type ='submit']").click()
print(driver.find_element(By.CLASS_NAME, "alert-success").is_displayed())
Message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(Message)
assert "Success" in Message
driver.find_element(By.XPATH ,"//input[@id ='inlineRadio1']").click()
driver.find_element(By.XPATH ,"(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH ,"(//input[@type='text'])[3]").clear()
#driver.find_element(By.CSS_SELECTOR , ".ng-valid").send_keys("Comments here")