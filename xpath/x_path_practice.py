from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

# Replace the file path with html
# for windows it will be like file://C:/Desktop/first.html
driver.get('file:///Users/chinna/Desktop/selenium/selenium/45-selenium/xpath/first.html')

# current_url function will not take any arguments and return the current url of the tab
print(driver.current_url)
import ipdb;ipdb.set_trace()
# h1 tag: x-path: //*[@id="h1Id"]
print(driver.find_element(By.XPATH, '//*[@id="h1Id"]').text)
print(driver.find_element(By.XPATH, '//*[@id="h1Id"]').get_attribute('class'))

# class --- ., id -- #
print(driver.find_element(By.CSS_SELECTOR, 'h1#h1Id').text)

# h1 tag: full x-path: /html/body/h1[1]
print(driver.find_element(By.XPATH, '/html/body/h1[1]').text)
print(driver.find_element(By.XPATH, '/html/body/h1[1]').get_attribute('class'))


print(driver.find_element(By.CSS_SELECTOR, 'p#pId1').text)
print(driver.find_element(By.CSS_SELECTOR, 'p[name="Hello hi how"]').text)


"""
<body>
    <div>
        <p>body.1div</p>
        <div>
            <p>body.2div</p>
            <div>
                <p>body.3div</p>
                <div>
                    <p id="div4">body.4div</p>
                    # print(driver.find_element(By.XPATH, '//*[@id="div4"]').text)
                    # print(driver.find_element(By.XPATH, 'html/body/div/div/div/div/p[1]').text)
                    # driver.find_element(By.CSS_SELECTOR, "p#div4").text
                    # print(driver.find_element(By.CSS_SELECTOR, 'body div div div div p').text)    
                    # print(driver.find_element(By.CSS_SELECTOR, 'html body div div div div p').text)
                </div>
            </div>
        </div>
    </div>
"""
# X-path
print(driver.find_element(By.XPATH, '//*[@id="div4"]').text)
print(driver.find_element(By.XPATH, 'html/body/div/div/div/div/p[1]').text)
# css
print(driver.find_element(By.CSS_SELECTOR, "p#div4").text)
print(driver.find_element(By.CSS_SELECTOR, 'html body div div div div p').text)
print(driver.find_element(By.CSS_SELECTOR, 'body div div div div p').text)
