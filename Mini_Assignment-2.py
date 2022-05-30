
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


# driver= webdriver.Chrome("/Users/sikalidas/PycharmProjects/Python_Selenium/Driver/chromedriver")
driver.get("http://webdriveruniversity.com/")

# ButtonClick

driver.find_element(By.XPATH,"(//div[@class='section-title'])[3]").click()

handles = driver.window_handles
size=len(handles)
for i in range(size):
    print()
    webele=driver.window_handles[i]
    driver.switch_to.window(webele)
driver.implicitly_wait(10)
driver.find_element(By.ID,'button1').click()
driver.find_element(By.XPATH,"//div[@class='modal-content']/div/button").click()
driver.implicitly_wait(20)



b = driver.find_element(By.CSS_SELECTOR,"span[id='button2']")
driver.execute_script("arguments[0].click();", b)
close=driver.find_element(By.XPATH,"//*[@id='myModalJSClick']/div/div/div[3]/button")
close.click()

b1 = driver.find_element(By.CSS_SELECTOR,"span[id='button3']")
driver.execute_script("arguments[0].click();", b1)
close=driver.find_element(By.XPATH,"//*[@id='myModalMoveClick']/div/div/div[3]/button")
close.click()

#Swith to main browser
webele=driver.window_handles[0]
driver.switch_to.window(webele)
#Dropdown and radio button
driver.find_element(By.XPATH,"(//div[@class='section-title'])[7]").click()
#
# driver.implicitly_wait(60)
# # Switch to child again
handles = driver.window_handles
size=len(handles)
for i in range(size):
    print()
    webele=driver.window_handles[i]
    driver.switch_to.window(webele)

# # # CHECKBOX
# Lista = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
# print(len(lista))
# for i in lista:
#     print(i.text())

# Dropdown
element=driver.find_element(By.ID,"dropdowm-menu-1")
drp=Select(element)
drp.select_by_visible_text("JAVA")
element1=driver.find_element(By.ID,"dropdowm-menu-2")
drp1=Select(element1)
drp1.select_by_index(2)
element2=driver.find_element(By.ID,"dropdowm-menu-3")
drp3=Select(element2)
drp3.select_by_value("javascript")

# Radio butoon
driver.find_element(By.XPATH,"//*[@id='radio-buttons']/input[4]").click()
verify=driver.find_element(By.XPATH,"//*[@id='radio-buttons']/input[4]").is_selected()
print("Radio button is selected : "+str(verify))

# Selected and disabled
verify1=driver.find_element(By.XPATH,"//*[@id='radio-buttons-selected-disabled']/input[2]").is_displayed()
print("Is the Radio buttton disabled :" + str(verify1))

veerify2=driver.find_element(By.XPATH,"//*[@id='fruit-selects']").is_selected()
print(veerify2)

# text
webele2=driver.window_handles[0]
driver.switch_to.window(webele2)

menu = driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'AUTOCOMPLETE TEXTFIELD')]")
menu.click()

driver.implicitly_wait(120)


#Switch to child
handles = driver.window_handles
size=len(handles)
for i in range(size):
    print()
    webele=driver.window_handles[i]
    driver.switch_to.window(webele)

driver.find_element(By.ID,"myInput").send_keys("P")
listname=driver.find_elements(By.XPATH,"//*[@id='myInputautocomplete-list']/div/input")
value="Pizza"



