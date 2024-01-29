from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginPage:
    ID_Username="Email"
    ID_Password="Password"
    Xpath_Submit="//button"
    Xpath_Logout="/html/body/div[3]/nav/div/ul/li[3]/a"

    def __init__(self,driver):
       self.driver=driver

    def SetUsername(self,email):
        self.driver.find_element(By.ID, self.ID_Username).clear()
        self.driver.find_element(By.ID,self.ID_Username).send_keys(email)

    def SetPassword(self, passw):
        self.driver.find_element(By.ID, self.ID_Password).clear()
        self.driver.find_element(By.ID, self.ID_Password).send_keys(passw)
    def Clicklogin(self):
        self.driver.find_element(By.XPATH,self.Xpath_Submit).click()

    def verifyTitle(self):
        #print(self.driver.title)
        return self.driver.title =='Dashboard / nopCommerce administration'

    def Clicklogout(self):
        self.driver.find_element(By.XPATH,self.Xpath_Logout).click()
