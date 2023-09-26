import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(f"file://{os.getcwd()}/alert3.html")
time.sleep(3)
#find_element_by_tag_name("button") will give the button element over which cilck() 
#function will do the cilck operation.
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(3)
#driver.switch_to.alert the alert object by which we get text, or we can accept / dismiss alert.
#In the below step i have assigned/ store the reference of alert obj in alert_obj
#returned by driver.switch_to.alert
alert_obj = driver.switch_to.alert

#.text with return the text of any element here it will return the text of alert.
print(alert_obj.text)
time.sleep(2)
# .send_keys() will take two argumnets one text to enter in input and other is keys
# and  insert the text in the alert text box 
#but here the text will enter in the input box only if you there is accept() function next 
#after using send_keys()
alert_obj.send_keys("siva")
time.sleep(3)
#.accept() will not take any agruments but accepts the alert/ click ok button
alert_obj.accept()

# #.dismiss() function won't take any agruments but dismiss the alert / click the cancel button
# alert_obj.dismiss()


time.sleep(5)
driver.close()