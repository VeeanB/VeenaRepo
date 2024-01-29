from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
import time
from selenium.webdriver.support.ui import Select

Service_obj=Service("C://chromedriver.exe")
#Service_obj=Service("C://geckodriver.exe")
ops=webdriver.ChromeOptions()
#ops=webdriver.FirefoxOptions()
ops.add_argument("--start-maximized")
ops.add_argument("--incognito")
#ops.add_argument("headless")
driver = webdriver.Chrome(service=Service_obj, options=ops)
act=ActionChains(driver)

#driver.maximize_window()
# driver.get("https://demoqa.com/select-menu")
# act=ActionChains(driver)
# #ele=ScrollOrigin.from_element(driver.find_element(By.ID,"cars"))
# ele=driver.find_element(By.ID,"cars")
# #act.scroll_to_element(ele).perform()
# driver.execute_script("arguments[0].scrollIntoView()",ele)
# #act.scroll_from_origin(ele,0,400).perform()
# act.key_down(Keys.CONTROL).move_to_element(driver.find_element(By.XPATH,"//option[@value='volvo']")).click().\
#     move_to_element(driver.find_element(By.XPATH,"//option[@value='saab']")).click().\
#     move_to_element(driver.find_element(By.XPATH,"//option[@value='opel']")).click().\
#     move_to_element(driver.find_element(By.XPATH,"//option[@value='audi']")).click().perform()
# print(driver.title)
# time.sleep(5)
#***************************************************Select option***********************************************************************
# driver.get("https://demoqa.com/select-menu")
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//*[@id='withOptGroup']/div[1]/div[2]/div").click()
# list=driver.find_elements(By.XPATH,"//*[@id='withOptGroup']/div[2]/div/div[2]/div/div")#unable to select
# print(len(list))
# for i in list:
#     #act.key_down(Keys.ARROW_DOWN).perform()
#
#     print(i.text)
#
#     #act.scroll_to_element(i).perform()
#     if 'Group 2 ,option 2' in i.text:
#         print("Clicked__")
#         i.click()
# time.sleep(5)
#****************************************************************************************************************************
# driver.find_element(By.XPATH,"//div[@id='selectOne']").click()
# list = driver.find_elements(By.XPATH,"//div[@class=' css-yt9ioa-option']")
# print(len(list))
# for i in list:
#      if 'Mr' in i.text:
#         i.click()
#      break
# time.sleep(5)
#*****************************************************************************************************************************
# drp = Select(driver.find_element(By.XPATH,'//*[@id="oldSelectMenu"]'))
# drp.select_by_visible_text("Yellow")
#**********************************************************Multiple selection*******************************************************************
# driver.find_element(By.XPATH,"//*[@id='selectMenuContainer']/div[7]/div/div/div/div[1]").click()
# mul=driver.find_elements(By.XPATH,"//*[@id='selectMenuContainer']/div[7]/div/div/div[2]/div/div")
# for i in mul:
#     #if i.text=='Blue': #Multiple selection
#         i.click()
#
#
#     #if i.text=='Black':
#      #   i.click()break
# time.sleep(10)
#*****************************************************************************************************************************
# driver.get("https://demoqa.com/accordian")
# driver.find_element(By.ID,"section1Heading").click()
# print(driver.find_element(By.ID,"section1Content").text)
# ele=driver.find_element(By.ID,"section2Heading").click()
# act.scroll_to_element(ele)
# print(driver.find_element(By.ID,"section2Content").text)
#******************************************************************************************************************************
#driver.get("https://demoqa.com/auto-complete")
#ime.sleep(5)
# driver.find_element(By.XPATH,"//input[@id='autoCompleteMultipleInput']").send_keys("R")
# mul=driver.find_elements(By.XPATH,"//div[@class='auto-complete__option css-yt9ioa-option']")
# for i in mul:
#     print(i.text)
#     i.click()
#     break
#*****************************************************************************************************************************
#driver.find_element(By.XPATH,"//input[@id='autoCompleteSingleInput']").send_keys("R")
#mul=driver.find_element(By.XPATH,"")
#*****************************************Slider************************************************************************************
# driver.get("https://demoqa.com/slider")
# ele=driver.find_element(By.XPATH,"//*[@id='sliderContainer']/div[1]/span/input")
# for i in range(75):
#     ele.send_keys(Keys.ARROW_RIGHT)
# print(ele.get_attribute("value"))
# #act.drag_and_drop_by_offset(ele,75,0)
# time.sleep(5)
#******************************************************************************************************************************
# driver.get("https://demoqa.com/tabs")
# driver.find_element(By.ID,"demo-tabpane-what").click()
# driver.find_element(By.ID,"demo-tab-origin").click()
# driver.find_element(By.ID,"demo-tab-use").click()
# print(driver.find_element(By.XPATH,"//div[3]/p").is_displayed())
#******************************************************************************************************************************
#driver.get("https://demoqa.com/sortable")
#s1=driver.find_element(By.XPATH,"//*[@id='demo-tabpane-list']/div/div[1]")
#d1=driver.find_element(By.XPATH,"//*[@id='demo-tabpane-list']/div/div[6]")
#Grid***************************************************
#driver.find_element(By.ID,"demo-tab-grid").click()
#s1=driver.find_element(By.XPATH,"//*[@id='demo-tabpane-grid']/div/div/div[1]")
#d1=driver.find_element(By.XPATH,"//*[@id='demo-tabpane-grid']/div/div/div[6]")
#act.drag_and_drop(s1,d1).perform()
#time.sleep(5)
#*********************************************************************************************************************************
# driver.get("https://demoqa.com/selectable")
# #driver.find_element(By.XPATH,"//*[@id='verticalListContainer']/li[1]").click()
# driver.find_element(By.ID,"demo-tab-grid").click()
# #ele=driver.find_elements(By.XPATH,"//*[@id='verticalListContainer']/li")
# ele=driver.find_elements(By.XPATH,"//div[@id='gridContainer']/div/li")
# print(len(ele))
# for i in ele:
#     i.click()
#     print(i.text)
#     print(driver.find_element(By.XPATH,"//li[@class='list-group-item active list-group-item-action']").is_displayed())
#    # print(driver.find_element(By.XPATH,"//li[@class='mt-2 list-group-item active list-group-item-action']").is_displayed())
# time.sleep(5)
#*******************************************************************Resizes*************************************************************
# driver.get("https://demoqa.com/resizable")
# ele=driver.find_element(By.XPATH,"//*[@id='resizableBoxWithRestriction']/span")
# print(ele.location)
# #ele1=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]")
# #act.drag_and_drop(ele,ele1).perform()
# act.drag_and_drop_by_offset(ele,300,100).perform()
# ele2=driver.find_element(By.XPATH,"//div[@id='resizable']/span")
# driver.execute_script("arguments[0].scrollIntoView()",ele2)
#
# #act.scroll_to_element(ele2)
# act.drag_and_drop_by_offset(ele2,300,100).perform()
#
#
# print(ele.location)
# time.sleep(10)
#**********************************************************************************************************************************
#driver.get("https://demoqa.com/droppable")
# s1=driver.find_element(By.ID,"draggable")
# d1=driver.find_element(By.ID,"droppable")
# act.drag_and_drop(s1,d1).perform()
# print(driver.find_element(By.XPATH,"//div[@class='drop-box ui-droppable ui-state-highlight']").is_displayed())
# time.sleep(5)
#*********************************************************************Acceptable***************************************************************
driver.get("https://demoqa.com/droppable")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='droppableExample-tab-accept']").click()
# s1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]")
# d1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]")
# #s1=driver.find_element(By.ID,"acceptable")
# #d1=driver.find_element(By.ID,"droppable")
# #act.scroll_to_element(s1).perform()
# #act.key_down(Keys.ARROW_DOWN).perform()
# time.sleep(5)
# #driver.execute_script("arguments[0].scrollIntoView()",s1,d1)
# act.drag_and_drop(s1,d1).perform()
# print(driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]").is_displayed()) #Not Working
#**************************************************************************************************************************************
# driver.find_element(By.ID,"droppableExample-tab-preventPropogation").click()
# s1=driver.find_element(By.ID,"dragBox")
# d1=driver.find_element(By.ID,"notGreedyInnerDropBox")
# act.drag_and_drop(s1,d1).perform()
# print(driver.find_element(By.XPATH,"//div[@class='drop-box-outer mt-4 ui-droppable ui-state-highlight']").is_displayed())
#************************************************Revert*****************************************************************************************
driver.find_element(By.ID,"droppableExample-tab-revertable").click()
s1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[1]/div[2]")
d1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[2]")
act.drag_and_drop(s1,d1).perform()  #Not working  both revert and not revert
time.sleep(5)
#******************************************************************************************************************************************
#driver.get("https://demoqa.com/dragabble")
# dr=driver.find_element(By.ID,"dragBox")
# print(dr.location)
# act.drag_and_drop_by_offset(dr,200,0).perform()
# print(dr.location)
#********************************************************************************************************************************************
# driver.find_element(By.ID,"draggableExample-tab-axisRestriction").click()
# x=driver.find_element(By.ID,"restrictedY")
# print(x.location)
# act.drag_and_drop_by_offset(x,0,100).perform()
# print(x.location)
#*********************************************************************************************************************************************
#driver.find_element(By.ID,"draggableExample-tab-containerRestriction").click()
#x=driver.find_element(By.XPATH,'//*[@id="containmentWrapper"]/div')
# x=driver.find_element(By.XPATH,"//*[@id='draggableExample-tabpane-containerRestriction']/div[2]/span")
# act.drag_and_drop_by_offset(x,0,200).perform()
#*********************************************************************************************************************************************
# driver.find_element(By.ID,"draggableExample-tab-cursorStyle").click()
# #x=driver.find_element(By.ID,"cursorCenter")
# #x=driver.find_element(By.ID,"cursorTopLeft")
# x=driver.find_element(By.ID,"cursorBottom")
# act.drag_and_drop_by_offset(x,0,-200).perform()
#************************************ProgressBar
# driver.get("https://demoqa.com/progress-bar")
# driver.find_element(By.ID,"startStopButton").click()
# time.sleep(5)
# print(driver.find_element(By.XPATH,"//div[@role='progressbar']").is_displayed())
# driver.find_element(By.ID,"startStopButton").click()
#***************************************************Menu Bar
# driver.get("https://demoqa.com/menu")
# menu=driver.find_element(By.XPATH,"//ul[@id='nav']/li[2]")
# menu1=driver.find_element(By.XPATH,"//*[@id='nav']/li[2]/ul/li[3]/a")
# menu2=driver.find_element(By.XPATH,"//*[@id='nav']/li[2]/ul/li[3]/ul/li[1]/a")
# act.move_to_element(menu).move_to_element(menu1).move_to_element(menu2).click().perform()
# time.sleep(5)