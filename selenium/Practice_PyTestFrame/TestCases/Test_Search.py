from time import sleep

from PageObject.LoginPage import LoginPage
from Utilities.readProperty import ReadConfig
from Utilities.customlogger import logger
from PageObject.Searchcustomer import SearchCustomers

class Test_Suit_Search():
    def  test_case_003_search(self,setup):
        self.User = ReadConfig.GetUsername()
        self.Password = ReadConfig.GetPassword()
        self.driver = setup
        self.log = logger()
        login_obj = LoginPage(self.driver)
        search_obj = SearchCustomers(self.driver)
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
        search_obj.ClickCustomerMenu()
        search_obj.ClickCustomerOption()
        #search_obj.SetCustomeremail("ztpc3@email.com")
        search_obj.SetCustomerfname("John")
        # search_obj.SetCustomerlname("Smith")
        # search_obj.SetMonth("6")
        # search_obj.SetDate("31")
        # search_obj.Setregistrationfrom("3/13/2017")
        # search_obj.Setregistrationto("3/13/2017")
        # search_obj.SetLastfrom("1/25/2024")
        # search_obj.SetLastto("1/25/2024")
        # search_obj.SearchCompany("test")
        # search_obj.SearchIP("162.158.8.141")
        # search_obj.CustomerRole("Registered")
        search_obj.Seachcustomer()
        print(search_obj.Verifyemaillist())
        self.status=search_obj.Verifyemaillist()
        # if self.status == True:
        #     self.log.info(" test_case_003_search :: Passed")
        #     assert True
        # else:
        #     self.driver.save_screenshot("./ScreenShots/ test_case_003_search.png")
        #     self.log.error(" test_case_003_search:: Failed")
        #     assert False

        sleep(10)



