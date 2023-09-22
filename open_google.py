from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.google.com/")
time.sleep(5)
driver.quit()

# quit : To close entair webdriver session
# close : to close the current page
