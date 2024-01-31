from time import sleep
import sys
sys.path.append(r'C:\Users\veenu\PycharmProjects\PythonClass\selenium\Practice_PyTestFrame')
print(sys.path)
from PageObject.LoginPage import LoginPage
from Utilities.readProperty import ReadConfig
from Utilities.customlogger import logger
#from PageObject.Searchcustomer import SearchCustomer
from PageObject.Addcustomer import Addcustomers



class Test_Suit_Addcustomer():
    def  test_case_001_addcustomer(self,setup):
       # search_obj=SearchCustomer(self.driver)
        self.User = ReadConfig.GetUsername()
        self.Password = ReadConfig.GetPassword()
        self.driver = setup
        self.log = logger()
        login_obj = LoginPage(self.driver)
        addcustomer_obj = Addcustomers(self.driver)
        login_obj.SetUsername(self.User)
        login_obj.SetPassword(self.Password)
        login_obj.Clicklogin()

        self.log.info("Login successful")
        if login_obj.verifyTitle() == True:
            self.log.info("test_case_001_login_title :: Passed")
            assert True
        else:
            self.log.error("test_case_001_login_title :: Failed")
            self.driver.save_screenshot(r".\ScreenShots\test_case_101_login_title.png")
            assert False
        addcustomer_obj.ClickCustomerMenu()
        addcustomer_obj.ClickCustomerOption()
        #addcustomer_obj.ClickCustomerInfo()
        sleep(5)
        addcustomer_obj.ClickAddCustomer()

        addcustomer_obj.SetCustomeremail(addcustomer_obj.randome_emailgen()+f"@gmail.com")
        addcustomer_obj.SetCustomerpassword("123")
        addcustomer_obj.SetFName("Vani")
        addcustomer_obj.SetLName("XYS")
        addcustomer_obj.SetGender("Male")
        addcustomer_obj.SetDOB("12/2/2024")
        addcustomer_obj.SetCompany("abc")
        addcustomer_obj.SetTaxempt("Yes")
        addcustomer_obj.SetNewsletters("Test store 2")
        addcustomer_obj.SetCustomerrole("Registered")
        addcustomer_obj.SetVendor("Vendor 1")
        addcustomer_obj.SetActive("Yes")
        addcustomer_obj.SetAdminComment()
        addcustomer_obj.ClickSave()
        sleep(10)
        print(addcustomer_obj.VerifyAlert())
        self.status=addcustomer_obj.VerifyAlert()
        if self.status == True:
            self.log.info("test_case_001_add_customer :: Passed")
            print("Passed")
            assert True
        else:
           self.log.error("test_case_001_add_customer :: Failed")
           self.driver.save_screenshot(r"C:\Users\veenu\PycharmProjects\PythonClass\selenium\Practice_PyTestFrame\ScreenShots\test_case_001_add_customer.png")
           assert False
