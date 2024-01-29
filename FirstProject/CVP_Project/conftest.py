import pytest
#from selenium.webdriver.chrome import webdriver
import selenium.webdriver.support.expected_conditions
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
       parser.addoption(
           "--browser_name", actions="store", default="chrome"
       )


@pytest.fixture(scope="class")
def setup(request):
    browser_name =request.config.getoption("browser_name")
    if browser_name == "chrome":
       service_obj = Service("C:/chromedriver.exe")
       driver = webdriver.Chrome(service=service_obj)
    #driver = webdriver.chrome(executable_path= "C:/Users/veenu/Documents/chromedriver_win32 (2)/chromedriver/chromedriver.exe")

       driver.maximize_window()
    elif browser_name == "firefox":
        service_obj = Service("C:/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
         print("IE driver")

    driver.get("http://cpv-nxg-dev.s3-website-us-east-1.amazonaws.com/")

    request.cls.driver = driver
    yield
    driver.close()




