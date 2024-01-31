import pytest
from PageObject.LoginPage import LoginPage
from Utilities.readProperty import ReadConfig
from Utilities.customlogger import logger

class Test_Suit_Login():
    def  test_case_001_login_title(self,setup):
        self.User = ReadConfig.GetUsername()
        self.Password=ReadConfig.GetPassword()
        self.driver=setup
        self.log = logger()
        login_obj = LoginPage(self.driver)
        login_obj.SetUsername(self.User)
        login_obj.SetPassword(self.Password)
        login_obj.Clicklogin()
        if login_obj.verifyTitle() == True:
            self.log.info("test_case_001_login_title :: Passed")
            assert True
        else:
            self.log.error("test_case_001_login_title :: Failed")
            self.driver.save_screenshot(r".\ScreenShots\test_case_101_login_title.png")
            assert False



        #login_obj.Clicklogout()
