#import pytest
from PageObject.LoginPage import Test_LoginPage
from Utilities.readProperty import ReadConfig
from Utilities.customlogger import logger


class TestCase_Suit_loginpage():

    def test_case_001_login_title(self,setup):
        self.User=ReadConfig.GetUsername()
        self.Passw=ReadConfig.GetPassword()
        self.driver=setup
        self.log=logger()
        login_obj = Test_LoginPage(self.driver)
        self.log.info("Test Case name::test_case_101_login_title")
        login_obj.SetUsername(self.User)
        login_obj.SetPassword(self.Passw)
        login_obj.ClickLogin()
        print(login_obj.Verify())
        if login_obj.Verify() == True:
            self.log.info("test_case_101_login_title :: Passed")
            assert True
        else:
             self.log.error("test_case_101_login_title :: Failed")
             self.driver.save_screenshot(r".\ScreenShots\test_case_001_login_title.png")
             assert False
             login_obj.Logout()






