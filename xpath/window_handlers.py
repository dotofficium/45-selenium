import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# import ipdb;ipdb.set_trace()
driver.maximize_window()

#Replace the file path with html
#for windows it will be like file://C:/Desktop/first.html

driver.get(f"file://{os.getcwd()}/fist.html")

#current_url function will not take any arguments and return the current url of the tab
print(driver.current_url)


"""
Switching the focus selenium from one tab to other
in the html on clicking the anchor tag it will open gmail in other window and but the focus of 
selenium will with the first tab only 
to change focus from one tab to other selenium provide some functions to handle the windows
"""
#current_window_handle will return the window which the selenium is focused on
print(driver.current_window_handle)
#on click the anchor tag it will open the google in other tab
driver.find_element(By.ID, 'id1').click()
time.sleep(5)
#after opening the new tab selenium will focused on the parent/first one only that you can see
#line number 25 and 31 will print that same because the focus of selenium is not changed
print(driver.current_window_handle)

#windows_handles will return the list with all the tab refernces as string
print(driver.window_handles)

time.sleep(5)
#switch_to_windows will return None but switch the focus of selenium to the specified tab
# here i was focusing to the newly opned tab i.e., second one in the window_hadles list.
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
#send_keys() method take two arguments one madidate and other is optional string that we enter in the input box.
#Other argument Kyes.ENTER will be discussed later.
#the below line in google.com we typing the text india in searchbox and hit enter of keyword with selenium
driver.find_element(By.NAME, 'q').send_keys('india', Keys.ENTER)
time.sleep(5)
#execute_script() function will take the javascript function as argument and execute it
#the below line it executing the function to scroll the window to bottom.
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(3)
#this line click the next button in the pagination
#about find_element_by_xpath will be discussed later
# driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
driver.find_element(By.XPATH, "//*/h3/div/span[2]").click()
time.sleep(1)
driver.close()
time.sleep(5)
driver.quit()

# and
# or
# contains
# starts-with