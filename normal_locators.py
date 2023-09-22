# drive
# get -- any url open
# drive -- attributes
#      print(dir(driver))
#     ('add_cookie', 'add_credential', 'add_virtual_authenticator', 'application_cache', 'back', 'bidi_connection',
#      'capabilities', 'caps', 'close', 'command_executor', 'create_web_element', 'current_url', 'current_window_handle',
#      'delete_all_cookies', 'delete_cookie', 'delete_network_conditions', 'desired_capabilities', 'error_handler',
#      'execute', 'execute_async_script', 'execute_cdp_cmd', 'execute_script', 'file_detector', 'file_detector_context',
#      'find_element', 'find_elements', 'forward', 'fullscreen_window', 'get', 'get_cookie', 'get_cookies',
#      'get_credentials', 'get_issue_message', 'get_log', 'get_network_conditions', 'get_pinned_scripts',
#      'get_screenshot_as_base64', 'get_screenshot_as_file', 'get_screenshot_as_png', 'get_sinks',
#      'get_window_position', 'get_window_rect', 'get_window_size', 'implicitly_wait', 'launch_app',
#      'log_types', 'maximize_window', 'minimize_window', 'mobile', 'name', 'orientation', 'page_source',
#      'pin_script', 'pinned_scripts', 'print_page', 'quit', 'refresh', 'remove_all_credentials', 'remove_credential',
#      'remove_virtual_authenticator', 'save_screenshot', 'service', 'session_id', 'set_network_conditions',
#      'set_page_load_timeout', 'set_permissions', 'set_script_timeout', 'set_sink_to_use', 'set_user_verified',
#      'set_window_position', 'set_window_rect', 'set_window_size', 'start_client', 'start_desktop_mirroring',
#      'start_session', 'start_tab_mirroring', 'stop_casting', 'stop_client', 'switch_to', 'timeouts', 'title',
#      'unpin', 'vendor_prefix', 'virtual_authenticator_id', 'window_handles')
# diff find_element and find_elements
#   find_element -- it will return 1st object
#   find_elements  -- list of matched objects
# Locators - ID, TAG, NAME, LINK_TEXT, PARTIAL_LINK_TEXT


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

# Replace the file path with html
# for windows it will be like file://C:/Desktop/first.html
driver.get('file:///Users/chinna/Desktop/selenium/selenium/45-selenium/first.html')

# current_url function will not take any arguments and return the current url of the tab
print(driver.current_url)

"""
Locators:
--Locators will helps selenium webdriver find the html element to perform the action
They are Two types of locators
1. Normal Locators
2. Customized Locators(css selector/xpath)

1.Normal Locators
 a. id:
    <h1 id="h1Id" class="h1Class">Second class</h1>
    The above is the h1 heading html tag for which there is attribute id with value "h1Id" by using this 
    we can locate this element.
    selenium provide the api or method find_element_by_id()
    find_element_by_id() takes one argumnet value of id of that element as mandiate argument
    and this returns the html element if Found else NoSuchElementException.
    *value of id should be provided as string.

b. name:
    <input id='inputId1' class='inputClass1' name='nameInput1' value="Hello world!"/>
    The above is Input thtml tag with having the "name" attribute with value "nameInput1" by using this we can 
    locate this element.
    selenium provide the api or method find_element_by_name()
    find_element_by_name() takes one argument value of name of that element as mandiate argument and
    this returns the html element if found else NoSuchElementException.
    *value of name should be provided as string.
c. class name:
     <p id='pId' class="pClass">This is second class of selenium and today we see how to get the data from tags,
         and window handling</p><br/>
    The above is paragraph tag  which  having the "class" attribute with value "pClass" by using this we can locate 
    this element.
    selenium provide the method find_element_by_class_name()
    find_element_by_class_name() takes one argumnet value of class pf that element as mandiate argument and
    this returns the html element if found else NoSuchElementException.
    *value of name should be provided as string.

d. tag_name:
    <a href="https://www.gmail.com/" target="_blank">Gmail.com</a><br/>
    The above is anchor tag which having the tag name "a" by using this we can locate this element.
    selenium provide the method find_element_by_tag_name()
    find_element_by_tag_name() takes one argumnet tag name as mandiate argument and returns the html element if found else
    NoSuchElementException.
    *Tag name should be provided as string.

e.link_text and partial_link_text:
    <a href="https://www.gmail.com/" target="_blank">Gmail.com</a><br/>
    The above link text or anchor tag has the text "Gmail.com" we can locate this element.
    selenium provide method find_element_by_link_text() and find_element_by_partial_link_text()
    both the method takes one mandiate arguments link_text() takes the exact text of that tag as argument 
    and partial_link_text() takes the any part of the text of that tag as argument.
    Both will return the html element if found else NoSuchEelementException.
    *text for link_text and partial_limk_text should be provide as string.

"""
anchor_tag = driver.find_element(By.TAG_NAME, 'h1')
import ipdb;ipdb.set_trace()
print(anchor_tag.text)
id = driver.find_element(By.ID, 'pId')
print(id.text)
print(id.get_attribute('id'))
name = driver.find_element(By.NAME, 'nameInput2')
print(name.get_attribute('placeholder'))
print(driver.find_element(By.LINK_TEXT, 'Gmail.com').text)
print(driver.find_element(By.PARTIAL_LINK_TEXT, 'Google').text)
print(driver.find_element(By.CLASS_NAME, 'h1Class').text)

# The above all find_elemnt_by functions contains other function like text, get_attribute,
# click() if it is clickable, send_keys() if it is input field , location etc, will be disscussed on later classes

# .text will return the actual text that is displaed in html
id = driver.find_element(By.ID, 'pId')
print(id.text)
# .get_attribute() will take one mandiate argument attribute of that element as string
# and return the value of that html element.
print(id.get_attribute('id'))
name = driver.find_element(By.NAME, 'nameInput2')

name.send_keys("Hi Sivareddy")
time.sleep(5)
print(name.get_attribute('placeholder'))

elements = driver.find_elements(By.TAG_NAME, "a")
for each in elements:
    print(each.get_attribute("href"))

driver.find_element(By.LINK_TEXT, 'Gmail.com').click()

time.sleep(5)
