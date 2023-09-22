from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/kothu/OneDrive/Documents/Selenium class/chromedriver/chromedriver')

driver.maximize_window()

#Replace the file path with html
#for windows it will be like file://C:/Desktop/first.html

driver.get('file://C:/Users/kothu/OneDrive/Documents/Selenium class/Day 2/first.html')

time.sleep(3)
element = driver.find_element(By.ID, "h11Id")
print(element.text)
print(element.get_attribute("class"))
time.sleep(3)
element = driver.find_element(By.CLASS_NAME, "h1Class")
print(element.text)
time.sleep(3)
element = driver.find_element(By.NAME, "nameInput2")
element.send_keys("Hello Siva")
time.sleep(3)
element = driver.find_element(By.TAG_NAME, "input")
element.send_keys("Siva reddy")
time.sleep(3)

# element = driver.find_element(By.LINK_TEXT, "Gmail.com")
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")
element.click()
time.sleep(3)

elements = driver.find_elements(By.TAG_NAME, "a")
for each in elements:
    print(each.text)
driver.quit()