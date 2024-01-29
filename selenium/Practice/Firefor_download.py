from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
import time
from selenium.webdriver.support.ui import Select
import os
location=os.getcwd()

Service_obj=Service("C://geckodriver.exe")
ops=webdriver.FirefoxOptions()
ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")#/msword,/txt,/pdf
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
ops.set_preference("bowser.download.manager.showWhenStarting",False)
ops.set_preference("browser.download.folderList",2)#0-desktop,1-downloadfolder,2-desiredloc
ops.set_preference("browser.download.dir",location)
driver = webdriver.Chrome(service=Service_obj, options=ops)

driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.find_element(By.XPATH, "//tbody/tr[1]/td/a[text()='Download sample DOC file']").click()
driver.maximize_window()
time.sleep(20)
