import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
driver.close()



