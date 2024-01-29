import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from PageObject.CheckOutPage import CheckOutPage
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


#from pageObjects.CheckoutPage import CheckOutPage
#from pageObjects.HomePage import HomePage
#from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkoutpage = CheckOutPage(self.driver)
       # cards = checkoutpage.getCardTitles ()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
                #self.driver.find_element(By.CSS_SELECTOR, "(.card-footer button)[i]").click()

        self.driver.find_elemen(By.CSS_SELECTOR ,"a[class*='btn-primary']").click()
        CheckOutPage.checkOutItems().click()


        #confirmpage = checkoutpage.checkOutItems()
        #log.info("Entering country name as ind")
        self.driver.find_element(By.ID,"country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        #log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
