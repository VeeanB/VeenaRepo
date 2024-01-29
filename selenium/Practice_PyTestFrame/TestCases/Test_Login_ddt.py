import pytest
import sys
from PageObject.LoginPage import LoginPage
from Utilities.readProperty import ReadConfig
from Utilities.customlogger import logger
from Utilities.Excelutils import *


class Test_Suit_Login():

        #path = r".\TestData\LoginData.xlsx"
        #sheet = "Sheet1"
        # print(getRow(path, sheet))
        # print(getCol(path, sheet))
        path=r"C:\Users\veenu\PycharmProjects\PythonClass\selenium\Practice_PyTestFrame\Test Data\TestData_DDT.xlsx"
        sheet = "Sheet1"
        print(getRow(path,sheet))
        print(getCol(path,sheet))
        data_list = []
        for i in range(2,getRow(path,sheet)+1):
            print((getValue(path,sheet,i,1),getValue(path,sheet,i,2),getValue(path,sheet,i,3)))
            data_list.append((getValue(path, sheet, i, 1), getValue(path, sheet, i, 2),getValue(path, sheet, i, 3)))
            print(data_list)
        #print(sheet1.max_row)
        @pytest.mark.parametrize('user,pswd,expected',data_list)
        def test_case_001_login_title(self, setup,user,pswd,expected):
            self.User = ReadConfig.GetUsername()
            self.Password = ReadConfig.GetPassword()
            self.driver = setup
            self.log = logger()
            login_obj = LoginPage(self.driver)
            login_obj.SetUsername(user)
            login_obj.SetPassword(pswd)
            login_obj.Clicklogin()
            print(login_obj.verifyTitle() == False)
            print(expected == "Fail")
            #print(expected)
            #print(login_obj.verifyTitle())
            if login_obj.verifyTitle() == True and expected == "Pass":
                self.log.info(f"test_case_001_login_title {user}_{pswd} :: Passed")
                login_obj.Clicklogout()
                assert True
            elif login_obj.verifyTitle() == False and expected == "Fail":
                self.log.info(f"test_case_102_login_title {user}_{pswd} :: Passed")
                assert True
            else:
                self.log.error(f"test_case_001_login_title {user}_{pswd} :: Fail")
                self.driver.save_screenshot(fr".\ScreenShots\test_case_101_login_title_{user}_{pswd}.png")
                assert False




