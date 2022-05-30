from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/sikalidas/PycharmProjects/Python_Selenium/Driver/chromedriver')


driver.get("http://webdriveruniversity.com/")
driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'SCROLLING AROUND')]").click()
wind=driver.current_window_handle
wind2=driver.window_handles[1]
driver.switch_to.window(wind2)


# Scroll
ele=driver.find_element(By.XPATH,"//*[@id='zone1']/h1")
action=ActionChains(driver)
action.move_to_element(ele).perform()
ele1=driver.find_element(By.XPATH,"//*[@id='zone1']")
tex="Well done for scrolling to me!"
string11= ele1.text
if string11==ele1:
    print("True")

ele2=driver.find_element(By.XPATH,"//*[@id='zone2-entries']")
action.move_to_element(ele2).perform()
ele3=driver.find_element(By.XPATH,"//*[@id='zone2-entries']")
string1= ele3.text
if string1==ele3:
    print("True")

ele4=driver.find_element(By.XPATH,"//*[@id='zone3-entries']")
action.move_to_element(ele4).perform()
ele5=driver.find_element(By.XPATH,"//*[@id='zone3-entries']")
string2= ele5.text
if string2==ele5:
    print("True")


ele6=driver.find_element(By.XPATH,"//*[@id='zone4']")
action.move_to_element(ele6).perform()
ele7=driver.find_element(By.XPATH,"//*[@id='zone4']")
string3= ele7.text
if string3==ele7:
    print("True")

print(driver.title)
webele=driver.window_handles[0]
driver.switch_to.window(webele)
print(driver.title)


