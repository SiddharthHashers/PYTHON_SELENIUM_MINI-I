from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# import time
# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/sikalidas/PycharmProjects/Python_Selenium/Driver/chromedriver')

# driver= webdriver.Chrome("/Users/sikalidas/PycharmProjects/Python_Selenium/Driver/chromedriver")
driver.get("https://www.goibibo.com/")

# # GOIBIBO LOGO
# driver.find_element(By.XPATH,"//span[@class='header-sprite logo']")

# Xpath
# # Login and Signup
# driver.find_element(By.XPATH,"//div[@class='login__tab gotrible']")


# relative Xpath
# # Fligts
# Flights=driver.find_element(By.LINK_TEXT,"Flights")
# print(Flights.text)

# Css selector
#Hotel
# class name -- span[class='header-sprite nav-icon-hotels gr-append-right5']
# driver.find_element(By.CSS_SELECTOR,"span[class='header-sprite nav-icon-hotels gr-append-right5']").click()



# # from
# driver.find_element(By.XPATH,"//p[class='sc-iJKOTD iipKRx fswWidgetPlaceholder'][1]")
#


# # to
# driver.find_element(By.XPATH,"//span[@class='sc-fHeRUh jHgPBA'][1]")

# student
# driver.find_element(By.XPATH,"//ul[@class='sc-iqseJM giZLuO']/li[4]").click()

# class name
#Products
# driver.find_element(By.CLASS_NAME,"fb button orange padLR30 txtTransUpper marginB10 fltHpySrchBtn").click()

#
# # Round trip
# driver.find_element(By.XPATH,"//ul[@class='sc-fvxzrP cCkBwj']/li[2]")

# wb=driver.find_element(By.XPATH,"//div[@class='txtCenter flexCol alignItemsCenter ']/a")
# wb.click()
# wb.click()
# #



# driver.close()