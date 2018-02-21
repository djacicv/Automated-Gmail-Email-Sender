# Python & Selenium Chrome Webdriver 
# Automated Gmail login and email sending
# Created on 21.02.2018 
# Created by vukasiN. 

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Username
user = "youremail@gmail.com"

# Password
pwd = "yourpassowrd"

# Recipient's email
email = "email@email.com"

# Subject
subject = "Automated Email" 

# Text
text = "This message is automated."

# Chrome Driver
driverpath = "Python36/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe" # put your path to chromedriver 

# Open Chrome
driver = webdriver.Chrome(driverpath)
driver.maximize_window()

# Open Gmail Page
driver.get("http://www.gmail.com")
time.sleep(2)

# Input Username or Email
element = driver.find_element_by_id("identifierId")
element.send_keys(user)
time.sleep(1)

# Press next for password
next = driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
time.sleep(1)

# Enter Password
element = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
element.send_keys("pwd")
time.sleep(1)

# Login Button
driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
time.sleep(4)

# Compose Button
driver.find_element_by_xpath("//*[@id=':uc']/div/div").click()
time.sleep(3)

# Input Recipient
driver.find_element_by_css_selector(".oj div textarea").send_keys(email)
time.sleep(1)

# Input Subject
driver.find_element_by_css_selector(".aoD.az6 input").send_keys(subject)
time.sleep(1)

# Input Text
driver.find_element_by_css_selector(".Ar.Au div").send_keys(text)
time.sleep(2)

# Send Button
driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3").click()
time.sleep(5)

# Close Browser
driver.close()
