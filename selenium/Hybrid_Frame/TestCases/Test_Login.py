import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObject.LoginPage import Loginpage
from Utilities.readProperty import ReadConfig
from Utilities.customLogger import logger


#from Hybrid_Frame.PageObject.LoginPage import Loginpage

class Test_Suite_001_login():
    def test_case_101_login_title(self,setup):

        self.User = ReadConfig.GetUsername()
        self.Pswd = ReadConfig.GetPassword()

        self.driver = setup
        self.log= logger()
        self.log.info("Test Case name: test_case_101_login_title")
        print(self.driver)

        login_obj=Loginpage(self.driver)
        login_obj.SetEmail(self.User)
        login_obj.SetPass(self.Pswd)
        login_obj.Submit()
        print(login_obj.verify())
        if login_obj.verify()==True:
            assert True
        else:
            self.driver.save_screenshot(r".\ScreenShots\test_case_101_login_title.png")
            assert False
            # print("Failure!!!")
            # assert False
        login_obj.Logout()



