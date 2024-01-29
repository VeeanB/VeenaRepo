from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.CSS_SELECTOR ,"a[href='/frames']").click()
driver.find_element(By.CSS_SELECTOR ,"a[href='/iframe']").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID ,"tinymce").clear()
driver.find_element(By.ID ,"tinymce").send_keys("Text Here for the Iframes")
driver.switch_to.default_content()
actual = driver.find_element(By.CSS_SELECTOR ,"h3").text
assert  actual == "An iFrame containing the TinyMCE WYSIWYG Editor"
