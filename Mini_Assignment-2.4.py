from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/sikalidas/PycharmProjects/Python_Selenium/Driver/chromedriver')
driver.get("http://webdriveruniversity.com/")



driver.find_element(By.XPATH,"//*[@id='actions']/div/div[1]").click()
child=driver.window_handles[1]
driver.switch_to.window(child)


source_element = driver.find_element(By.XPATH,"//*[@id='draggable']")
dest_element = driver.find_element(By.XPATH,"//*[@id='droppable']")
ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
ele=driver.find_element(By.XPATH,"//*[@id='double-click']/h2")
ActionChains(driver).double_click(ele).perform()

ele4=driver.find_element(By.XPATH,"//*[@id='div-hover']/div[1]/button")
action=ActionChains(driver)
action.move_to_element(ele4).perform()




element = driver.find_element(By.XPATH,"//*[@id='click-box']")

action = ActionChains(driver)
click = ActionChains(driver)
action.click_and_hold(element)
action.perform()
time.sleep(10)
action.release(element)
action.perform()
time.sleep(0.2)
action.release(element)