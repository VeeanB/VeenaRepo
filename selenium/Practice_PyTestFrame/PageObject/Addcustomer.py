from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import string
import random


class Addcustomers:
    Xpath_customer_menu="//ul[@role='menu']/li[4]/a/p"
    Xpath_customer_option="//ul[@role='menu']/li[4]/ul/li[1]/a/p"
    Xpath_add="//a[@class='btn btn-primary']"
    Xpath_Custominf="//button[@class='btn btn-tool']/i"
    Id_Email="Email"
    Id_Password="Password"
    Id_Fname="FirstName"
    Id_Lname="LastName"
    Id_GenderM="Gender_Male"
    Id_GenderF = "Gender_Male"
    Id_DOB="DateOfBirth"
    Id_Company="Company"
    Id_Tax="IsTaxExempt"
    Xpath_NewSletter="//input[@aria-describedby='SelectedNewsletterSubscriptionStoreIds_taglist']"
    newsletter_option = "Test store 2"
    xpath_option_newsletter = f"//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[contains(text(),'{newsletter_option}')]"
    Id_Customerole="SelectedCustomerRoleIds"
    customerrole_option = 'Guests'
    xpath_customerrole_container = "//input[@aria-describedby='SelectedCustomerRoleIds_taglist']"
    xpath_customerrole = f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{customerrole_option}')]"
    xpath_defaultregisterrole = "//span[contains(text(),'Registered')]"
    xpath_deleteregisterrole = "//span[contains(text(),'Registered')]/following-sibling::span"
    Id_Managervendor="VendorId"
    id_active = "Active"
    Id_Comment="AdminComment"
    Xpath_Save="//button[@name='save']"
    Xpath_Alert="//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
      self.driver=driver

    def ClickCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.Xpath_customer_menu).click()

    def ClickCustomerOption(self):
        self.driver.find_element(By.XPATH,self.Xpath_customer_option).click()
    def ClickCustomerInfo(self):
        self.driver.find_element(By.XPATH,self.Xpath_Custominf).click()

    def ClickAddCustomer(self):
        self.driver.find_element(By.XPATH, self.Xpath_add).click()

    def SetCustomeremail(self,email):
        self.driver.find_element(By.ID,self.Id_Email).send_keys(email)

    def SetCustomerpassword(self,paswd):
        self.driver.find_element(By.ID,self.Id_Password).send_keys(paswd)

    def SetFName(self,Fname):
        self.driver.find_element(By.ID,self.Id_Fname).send_keys(Fname)

    def SetLName(self,Lname):
        self.driver.find_element(By.ID,self.Id_Lname).send_keys(Lname)

    def SetGender(self,gender):
        if gender =="Male":
         self.driver.find_element(By.ID,self.Id_GenderM).click()
        elif gender == "Female":
          self.driver.find_element(By.ID,self.Id_GenderF).click()
        else:
            self.driver.find_element(By.ID,self.Id_GenderM).click()

    def SetDOB(self,DOB):
        self.driver.find_element(By.ID,self.Id_DOB).send_keys(DOB)

    def SetCompany(self,company):
        self.driver.find_element(By.ID,self.Id_Company).send_keys(company)

    def SetTaxempt(self,option):
        if option == 'Yes':
          self.driver.find_element(By.ID,self.Id_Tax).click()
        elif option =='No':
            pass
    def SetNewsletters(self,NL_name):
        self.driver.find_element(By.XPATH, self.Xpath_NewSletter).click()
        self.newsletter_option = NL_name
        self.driver.find_element(By.XPATH, self.xpath_option_newsletter).click()
    def SetCustomerrole(self,role):
        self.customerrole_option = role
        sleep(3)
        if role == "Registered":
            if self.driver.find_element(By.XPATH, self.xpath_defaultregisterrole).is_displayed():
                pass
            elif self.driver.find_element(By.XPATH, self.xpath_defaultregisterrole).is_displayed() == False:
                self.driver.find_element(By.XPATH, self.xpath_customerrole_container).click()
                # self.driver.find_element(By.XPATH, self.xpath_customerrole).click()
                self.driver.find_element(By.XPATH,
                                         f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{self.customerrole_option}')]").click()
        if role != "Registered":
            self.driver.find_element(By.XPATH, self.xpath_deleteregisterrole).click()
            self.driver.find_element(By.XPATH, self.xpath_customerrole_container).click()
            # self.driver.find_element(By.XPATH, self.xpath_customerrole).click()
            self.driver.find_element(By.XPATH,f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{self.customerrole_option}')]").click()
    def SetVendor(self,Vname):
        self.drp_down = Select(self.driver.find_element(By.ID, self.Id_Managervendor))
        self.drp_down.select_by_visible_text(Vname)
    def SetActive(self, option):
        if option=="No":
            self.driver.find_element(By.ID, self.id_active).click()
        elif option=="Yes":
            pass

    def SetAdminComment(self):
        msg = "this is admin content"
        self.driver.find_element(By.ID, self.Id_Comment).send_keys(msg)

    def ClickSave(self):
        self.driver.find_element(By.XPATH,self.Xpath_Save).click()

    def VerifyAlert(self):
        return "The new customer has been added successfully." in self.driver.find_element(By.XPATH, self.Xpath_Alert).text
        #return(self.driver.find_element(By.XPATH,self.Xpath_Alert).text)

    def randome_emailgen(self):
        email_gen=""
        for i in range(8):
            email_gen=email_gen+ random.choice(string.ascii_letters+string.digits)
        return email_gen










