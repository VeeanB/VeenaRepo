from selenium import webdriver
from selenium.webdriver.common.by import By

class Loginpage:
  Id_email="Email"
  Id_pass="Password"
  Xpath_Submit="//button[@type='submit']"
  Xpath_Logout="//a[contains(text(),'Logout')]"

  def __init__(self, driver):
      self.driver = driver

  def SetEmail(self, email):
      self.driver.find_element(By.ID, self.Id_email).clear()
      self.driver.find_element(By.ID, self.Id_email).send_keys(email)

  def SetPass(self, passwd):
      self.driver.find_element(By.ID, self.Id_pass).clear()
      self.driver.find_element(By.ID, self.Id_pass).send_keys(passwd)

  def Submit(self):
      self.driver.find_element(By.XPATH, self.Xpath_Submit).click()

  def verify(self):
      return self.driver.title == "Dashboard / nopCommerce administration"


  def Logout(self):
      self.driver.find_element(By.XPATH, self.Xpath_Logout).click()



