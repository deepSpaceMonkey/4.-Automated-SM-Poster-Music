from selenium import webdriver
#!/usr/local/bin/python

from selenium.webdriver.support.ui import WebDriverWait

# Step 1) Open Firefox
# browser = webdriver.Chrome('/Users/bigboi/Desktop/chromedriver')
# # Step 2) Navigate to Facebook
# browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
# # Step 3) Search & Enter the Email or Phone field & Enter Password
# username = browser.find_element_by_id("username")    # Found using inspect element
# username.send_keys("<usernameGoesHere>")
# password = browser.find_element_by_id("password")    # Found using inspect element
# password.send_keys("<passwordGoesHere>")
#
# '''
# Inspect Element, click on the web object,
# right click on html code, copy->xpath
# '''
# logInButton = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/form/div[3]/button")
#
# # Step 4) Click Login
# logInButton.click()
#
# enterPost = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[1]/div/div[1]/button")
# enterPost.send_keys("<postGoesHere>")
# postText = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/button/span")
# postText.click()

import platform
y = platform.system()
print y

# If mac system, then open Chrome from hard drive
if y == 'Darwin':
     browser = webdriver.Chrome("/Volumes/BigBoi/Selenium_Project/chromedriver")
