from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomers:
    Xpath_customer_menu = "//ul[@role='menu']/li[4]/a/p"
    Xpath_customer_option = "//li[4]/ul[@class='nav nav-treeview']/li/a/p[contains(text(),'Customers')]"
    Id_SEmail="SearchEmail"
    Id_SFname="SearchFirstName"
    Id_SLname="SearchLastName"
    ID_select_month="SearchMonthOfBirth"
    ID_select_Date="SearchDayOfBirth"
    ID_Registration_From="SearchRegistrationDateFrom"
    ID_Registration_To="SearchRegistrationDateTo"
    Id_Last_From="SearchLastActivityFrom"
    Id_Last_To="SearchLastActivityTo"
    Id_Searchcompany="SearchCompany"
    Id_SearchAddress="SearchIpAddress"
    Id_CustomerRole="SelectedCustomerRoleIds"
    customerrole_option = 'Forum Moderators'
    xpath_customerrole = f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{customerrole_option}')]"
    xpath_defaultregisterrole = "//span[contains(text(),'Registered')]"
    xpath_deleteregisterrole = "//span[contains(text(),'Registered')]/following-sibling::span"
    Id_Searchbtn="search-customers"
    Xpath_emaillist="//table[@id='customers-grid']/tbody/tr/td[2]"
    Xpath_Firstnamelist="//table[@id='customers-grid']/tbody/tr/td[3]"

    def __init__(self,driver):
      self.driver=driver

    def ClickCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.Xpath_customer_menu).click()

    def ClickCustomerOption(self):
        self.driver.find_element(By.XPATH,self.Xpath_customer_option).click()

    def SetCustomeremail(self, email):
        self.driver.find_element(By.ID, self.Id_SEmail).send_keys(email)

    def SetCustomerfname(self, Fname):
        self.driver.find_element(By.ID, self.Id_SFname).send_keys(Fname)
    def SetCustomerlname(self,Lname):
        self.driver.find_element(By.ID, self.Id_SLname).send_keys(Lname)

    def SetMonth(self,month):
        month="6"
        mon=Select(self.driver.find_element(By.ID,self.ID_select_month))
        mon.select_by_visible_text(month)
    def SetDate(self,date):
        date="25"
        day=Select(self.driver.find_element(By.ID,self.ID_select_Date))
        day.select_by_visible_text(date)
    def Setregistrationfrom(self,RFdate):
        self.driver.find_element(By.ID,self.ID_Registration_From).send_keys(RFdate)

    def Setregistrationto(self,RTdate):
        self.driver.find_element(By.ID,self.ID_Registration_To).send_keys(RTdate)

    def SetLastfrom(self,LFdate):
        self.driver.find_element(By.ID,self.Id_Last_From).send_keys(LFdate)

    def SetLastto(self,LTdate):
        self.driver.find_element(By.ID,self.Id_Last_To).send_keys(LTdate)

    def SearchCompany(self,company):
        self.driver.find_element(By.ID,self.Id_Searchcompany).send_keys(company)

    def SearchIP(self,IP):
        self.driver.find_element(By.ID,self.Id_SearchAddress).send_keys(IP)

    def CustomerRole(self,role):
        self.customerrole_option = role
        if role=="Registered":
            if  self.driver.find_element(By.XPATH, self.xpath_defaultregisterrole).is_displayed():
                pass
            elif self.driver.find_element(By.XPATH, self.xpath_defaultregisterrole).is_displayed()==False:
                self.driver.find_element(By.XPATH, self.xpath_customerrole ).click()
                self.driver.find_element(By.XPATH, self.xpath_customerrole).click()
        if role != "Registered":
            self.driver.find_element(By.XPATH, self.xpath_deleteregisterrole).click()
            self.driver.find_element(By.XPATH, self.xpath_customerrole ).click()
            self.driver.find_element(By.XPATH, self.xpath_customerrole).click()

    def Seachcustomer(self):
        self.driver.find_element(By.ID,self.Id_Searchbtn).click()

    def Verifyemaillist(self):
        #print(self.driver.find_element(By.XPATH,self.Xpath_emaillist).text)
        #return "admin@yourStore.com" in (self.driver.find_element(By.XPATH,self.Xpath_emaillist).text)
        list = self.driver.find_elements(By.XPATH,self.Xpath_Firstnamelist)
        print(len(list))
        fname="John"
        for i in list:
             print(i.text)
             if  fname in i.text:
                 break
             # else:
             #    self.driver.find_element(By.XPATH,"//ul[@class='pagination']/li[3]/a").click()

        #print("passed")
        return fname










