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

driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'TO DO LIST')]").click()
A=driver.window_handles[1]
driver.switch_to.window(A)


wb=driver.find_element(By.CSS_SELECTOR,"#container > input[type=text]")
wb.click()
wb.send_keys("apple",Keys.ENTER)

ele=driver.find_element(By.XPATH,"//*[@id='container']/ul/li[1]")
action=ActionChains(driver)
action.move_to_element(ele).perform()

ele1=driver.find_element(By.XPATH,"//*[@id='container']/ul/li[1]/span/i")
ele1.click()

