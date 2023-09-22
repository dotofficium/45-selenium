from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.google.com/")
time.sleep(5)
import ipdb;ipdb.set_trace()
# find_element
# find_elemnts
print(driver.find_elements("name", "app"))
print(driver.find_elements("name", "referrer"))

driver.quit()