import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from Utilities.readProperty import ReadConfig

@pytest.fixture()
def setup(browser):
    print(browser)
    BaseURL = ReadConfig.GetBaseUrl()
    if browser != None:
        if browser.lower() == "chrome":
            from selenium.webdriver.chrome.service import Service
            service_obj = Service(r"C:\chromedriver.exe")
            driver = webdriver.Chrome(service=service_obj)
        elif browser.lower() == "edge":
            from selenium.webdriver.edge.service import Service
            service_obj = Service(r"C:\msedgedriver.exe")
            driver = webdriver.Edge(service=service_obj)
        elif browser.lower() == "firefox":
            from selenium.webdriver.firefox.service import Service
            service_obj = Service(r"C:\geckodriver.exe")
            driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    driver.get(BaseURL)
    driver.maximize_window()
    yield driver
    driver.quit()

  #       if browser== "chrome":
  #           from selenium.webdriver.chrome.service import Service
  #           service_obj = Service(r"C:\chromedriver.exe")
  #           driver = webdriver.Chrome(service=service_obj)
  #       elif browser == "firefox":
  #           from selenium.webdriver.firefox.service import Service
  #
  #           service_obj = Service(r"C:\geckodriver.exe")
  #           driver = webdriver.Firefox(service=service_obj)
  #       elif browser== "edge":
  #           from selenium.webdriver.edge.service import Service
  #
  #           service_obj = Service(r"C:\msedgedriver.exe")
  #           driver = webdriver.Edge(service=service_obj)
  #
  # #  else:
  #  #     from selenium.webdriver.chrome.service import Service
  #   #    service_obj = Service(r"C:\chromedriver.exe")
  #    #   driver = webdriver.Chrome(service=service_obj)
  #   #driver.get("https://admin-demo.nopcommerce.com/")
  #   driver.get(BaseURL)
  #   driver.maximize_window()
  #   yield driver
  #   driver.quit()



def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    print(request.config.getoption("--browser"))
    return request.config.getoption("--browser")



