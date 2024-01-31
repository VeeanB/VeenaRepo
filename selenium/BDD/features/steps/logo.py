from time import sleep
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given(u'Launch the browser')
def step_impl(context):
    #s=Service("C://chromedriver.exe")
    context.driver=webdriver.Chrome(service=Service("C:\\chromedriver.exe"))

@when(u'Go to the nobcommerace url')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")

@then(u'Verify logo')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//h1")

@when(u'navigate to the application')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")

@when(u'enter  "{username}" and "{password}"')
def step_impl(context,username,password):
    context.driver.find_element(By.ID,"Email").clear()
    context.driver.find_element(By.ID,"Email").send_keys(username)
    context.driver.find_element(By.ID, "Password").clear()
    context.driver.find_element(By.ID, "Password").send_keys(password)

@when(u'click on submit button')
def step_impl(context):

   context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
   sleep(5)

@then(u'verify the dashboard heading in the home page')
def step_impl(context):
   if context.driver.find_element(By.XPATH,"//h1[contains(text(), 'Dashboard')]").is_displayed():
       print("Dashboard page launched successfully")
   else:
       assert False

@then(u': Close Browser')
def step_impl(context):
    context.driver.quit()


