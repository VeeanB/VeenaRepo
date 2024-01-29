from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Edge
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#(//input[@type='checkbox'])[2] selecting 2 option from check box

dropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
dropdown.select_by_visible_text("Option2")


checkboxes = driver.find_elements(By.XPATH , "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("name") == "checkBoxOption2":
        checkbox.click()
        assert  (checkbox.is_selected())
        break

radios = driver.find_elements(By.XPATH , "//input[@type='radio']")
print(len(radios))

for radio in radios:
   if radio.get_attribute("value") =="radio2":
    radio.click()
    assert (radio.is_selected())
    break
assert driver.find_element(By.ID , "displayed-text").is_displayed()
driver.find_element(By.ID ,"hide-textbox").click()
assert not driver.find_element(By.ID , "displayed-text").is_displayed()


