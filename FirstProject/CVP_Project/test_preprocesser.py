import string
from random import random
import time

import pytest
import selenium.webdriver.support.expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")

class TestOne(BaseClass):
        def test_login(self):
          #service_obj = Service("C:/chromedriver.exe")
          #driver = webdriver.Chrome(service=service_obj)
          # driver = webdriver.chrome(executable_path= "C:/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver/chromedriver.exe")
          #driver.get("http://cpv-nxg-dev.s3-website-us-east-1.amazonaws.com/")
          #driver.maximize_window()
          #self.driver.find_element(By.XPATH ,"//button[normalize-space()='Logout from all devices']").click()
          #time.sleep(10)
          self.driver.find_element(By.NAME, "email").send_keys("ShalakaPreProcessor")
          self.driver.find_element(By.NAME, "password").send_keys("Shalaka@123")
          self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
          time.sleep(7)
          self.driver.find_element(By.CSS_SELECTOR,".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.btn-create-new-project.css-gb4vjp").click()
          element =self.driver.find_element(By.XPATH,"//input[@id=':r0:']")
          randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
          element.send_keys(randstring)
          #dropdown = Select(self.
          self.driver.find_element(By.XPATH, "//div[@role='button']")
          self.driver.find_element(By.XPATH, "(//li[@role='option'])[1]").click()
          #dropdown.select_by_visible_text("CAR_NK")
          #dropdown.select_by_index(1)
          self.driver.find_element(By.XPATH ,"//button[normalize-space()='Continue']").click()
          sample1=Select(self.driver.find_element(By.XPATH ,"//div[@id='demo-select-small']"))
          sample1.select_by_index(0)
          time.sleep(4)
          self.driver.find_element(By.XPATH, "//div[@id='demo-select-small']").close()
          self.driver.find_element(By.ID,":r2:").send_keys("Tag1")
          self.driver.find_element(By.CLASS_NAME ,"MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium btn-contained css-1ilfqp6").click()
          template =Select(self.driver.find_element(By.XPATH ,"//li[normalize-space()='Sample_Extraction_Template.xlsx'"))
          template.select_by_index(0)
          template1=Select(self.driver.find_element(By.XPATH ,"//li[normalize-space()='Sample_Extraction_Template_Output_Format.xlsx']"))
          template1.select_by_index(0)
          self.driver.find_element(By.XPATH ,"//button[normalize-space()='Continue'").click()



