from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import autoit

s=Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
# driver.get("https://demo.opencart.com/")
# driver.implicitly_wait(10)
# ele=driver.find_elements(By.XPATH,"//div[@class='row']/div/form/div/div[2]/div/h4/a")
# print(len(ele))
# for i in ele:
#
#     if i.text=='iPhone':
#         print(i.find_element(By.XPATH, "//div[@class='price']").text)
#         i.click()
#         sleep(10)
#         break
# driver.find_element(By.ID,"input-quantity").clear()
# driver.find_element(By.ID,"input-quantity").send_keys("3")
# driver.find_element(By.ID,"button-cart").click()
# print(driver.find_element(By.XPATH,"//div[@id='alert']/div").text)
# sleep(10)

#***********************************************************************************************************************
# driver.get("https://www.bedbathandbeyond.com/c/cookware/cookware-sets?t=24679")
# sleep(10)
# driver.find_element(By.XPATH,"//div[@class='priceContainer price_container__jbAh_']").click()
# p1,c1=driver.window_handles
# driver.switch_to.window(c1)
# print(driver.find_element(By.XPATH,"//section[@class='css-gx0lhm e14riyry2']/h1").text)
# print(driver.find_element(By.XPATH,"//div[@class='css-1tlmwo2 e1rnmadm1']/div/div[2]").text)
# qty=Select(driver.find_element(By.ID,"quantity"))
# qty.select_by_value("4")
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//button[@class='css-myk00y e161leko6']").click()
#***********************************************************************************************************************
driver.get("https://www.bedbathandbeyond.com/c/bedding/comforters-and-sets?t=50")
sleep(20)
# driver.find_element(By.XPATH,'//*[@id="products"]/article/a/div/div/p[contains(text(),"Long Plush Shaggy Comforter Set")]').click()
# parent,child=driver.window_handles
# driver.switch_to.window(child)
# qty=Select(driver.find_element(By.XPATH,"//select[@id='quantity']"))
# qty.select_by_value("4")
# driver.find_element(By.XPATH,"//*[@id='page-wrap']/main/div/div/div[2]/section[2]/section/div/div[1]/div[2]/button[1]/span").click()
# driver.find_element(By.XPATH,"//div/button[@class='cl-image-chip-button cl-image-chip-button-large'][1]/div[text()='Dark Gray'] ").click()
# #driver.find_element(By.XPATH,"//button[@class='cl-button cl-button-lg cl-button-alt-primary  css-1x0359 e161leko12']").click()
# driver.find_element(By.XPATH,"//button[@class='css-1q7tmz3 e161leko6']").click()
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//div[@id='scrollingContainer']/div/section/span[@data-cy='add-promo-code']").click()
# driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/section/div[2]/div[2]/div/div/section/div/div/div/input").send_keys("TYSQ67")
# driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/section/div[2]/div[2]/div/div/section/div/button").click()



#/html/body/div[@id='__next']/div[@id='search-nav-page']/div[@id='bd']/main[@id='sn-wrapper']/section/section[@id='products']/article/a/div[2]/div[4]/p

ele=driver.find_elements(By.XPATH,"//section[@id='products']/article/a/div[2]/div[4]/p")
print(len(ele))
for i in ele:
    print(i.text)
    if i.text=='Long Plush Shaggy Comforter Set':
        i.click()
        driver.implicitly_wait(10)
        parent,child=driver.window_handles
        driver.switch_to.window(child)
        driver.find_element(By.XPATH,"//*[@id='page-wrap'']/main/div/div/div[2]/section[2]/section/div/div[2]/div[2]/div/button[1]/div[2] ").click()
        driver.find_element(By.XPATH,"//button[@class='cl-button cl-button-lg cl-button-alt-primary  css-1x0359 e161leko12']").click()
        driver.find_element(By.XPATH,"//button[@class='css-1q7tmz3 e161leko6']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//div[@id='scrollingContainer']/div/section/span[@data-cy='add-promo-code']").click()
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/section/div[2]/div[2]/div/div/section/div/div/div/input").send_keys("TYSQ67")
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/main/section/div[2]/div[2]/div/div/section/div/button").click()
    break
