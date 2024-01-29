import unittest
from selenium.webdriver.chrome.service import Service

import tests2
from selenium import webdriver


class test_case(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("Loggin method in setup ")


    @classmethod
    def setUpClass(cls):
        print("Login in setup class")

    @classmethod
    def tearDown(self):
        print("Logout method in teardown")


    @classmethod
    def tearDownClass(cls):
        print("Logout in teardown class")


    def test_case1(self):
        print("Test case first is executed")
        s = Service("C://chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(driver.title)

        self.assertEqual('OrangeHRM', driver.title, "title not same")

    def test_case2(self):
        print("test case second is executed")




if __name__== "__main__":
    unittest.main()