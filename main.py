from selenium import webdriver
import platform

y = platform.system()    # Find out the OS because different file paths
if y == 'Windows':
    browser = webdriver.Chrome(r"D:\pythonProject_Aug21\chromedriverWIN.exe")

elif y == 'Darwin':
    browser = webdriver.Chrome(r"/Volumes/BOOPC/pythonProject_Aug21/chromedriverOSX")

# Enter the website URLs
# Use <r""> to convert from normal string to raw string (used when exiting)
LinkedInURL = r"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
FaceBookURL = r"https://www.facebook.com/"
SpotifyURL = r"https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F"

from selenium.webdriver.common.keys import Keys
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



#     # USE R to convert normal string to raw string, or put file path in a variable string
# Ask the websites for trust certificate so no need for webistes, chrome stores in ones place so when u log in to chrome, it automaticly bypasses all of it
# bypass/automate the authentication process with trust certificates
# have the program run from a phone instead of hard drive

# If mac system, then open Chrome from hard drive
# if y == 'Darwin':
#     browser = webdriver.Chrome("/Volumes/BigBoi/Selenium_Project/chromedriverOSX")
browser.get(LinkedInURL)
browser.implicitly_wait(3)
# browser.execute_script("window.open('' + FaceBookURL, 'new window')")  # opens FB in new tab
# browser.implicitly_wait(3)
# body = browser.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL + 't')
# browser.send_keys(Keys.COMMAND + Keys.t)
# # browser.get("https://www.facebook.com/")
