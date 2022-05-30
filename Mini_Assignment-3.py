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
driver.get("https://the-internet.herokuapp.com/")


driver.implicitly_wait(10)

click1=driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
click1.click()
a = driver.switch_to.alert
print(a.text)
driver.switch_to.alert.accept()
result=driver.find_element(By.XPATH,"//p[@id='result']")
print(result.text)
time.sleep(5)


click2=driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
click2.click()
a = driver.switch_to.alert
print(a.text)
driver.switch_to.alert.accept()
result=driver.find_element(By.XPATH,"//p[@id='result']")
print(result.text)
time.sleep(5)


click3=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
click3.click()
a = driver.switch_to.alert
print(a.text)
alert = driver.switch_to.alert
alert.send_keys('selenium')
time.sleep(5)
driver.switch_to.alert.accept()
result=driver.find_element(By.XPATH,"//p[@id='result']")
print(result.text)


