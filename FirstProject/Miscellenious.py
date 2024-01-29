from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless") # to run headless mode
chrome_option.add_argument("--ignore-certificate-errors")#certificates related messages

#from selenium.webdriver.firefox.service import Service
#Edge
service_obj = Service("/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver")
driver = webdriver.Chrome(service=service_obj , options=chrome_option)

driver.implicitly_wait(5)
driver.maximize_window()
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")