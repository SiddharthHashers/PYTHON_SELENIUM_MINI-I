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
driver.get("https://weathershopper.pythonanywhere.com/")
ele = driver.find_element(By.XPATH, "//div[@class='row panel justify-content-center col-4 offset-4']/div/span")
print(ele.text)

ele1=driver.find_element(By.XPATH,"//span[@class='octicon octicon-info']")
ele1.click()