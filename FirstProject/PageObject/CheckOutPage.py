from selenium.webdriver.common.by import By


class CheckOutPage:
    def __int__(self,driver):
        self.driver = driver
    cardTitle= (By.CSS_SELECTOR,".card-title a")
    cardFooter=(By.CSS_SELECTOR,".card-footer button")
#driver.find_element(By.CSS_SELECTOR,".card-title a")
    checkOut = (By.XPATH, "//button[@class='btn btn success']")

    def getCardTitles(self):

          return  self.driver.find_elements(*CheckOutPage.cardTitle)


    def getCardFooter(self):

           return self.driver.find_elements(*CheckOutPage.cardFooter)


    def checkOutItems(self):

           return self.driver.find_element(*CheckOutPage.checkOut)

