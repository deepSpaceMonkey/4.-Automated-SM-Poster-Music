from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform
import time
import spotipy


y = platform.system()    # Find out the OS because different file paths
if y == 'Windows':
    browser = webdriver.Chrome(r"D:\pythonProject_Aug21\chromedriverWIN.exe")

elif y == 'Darwin':
    browser = webdriver.Chrome(r"/Volumes/BOOPC/pythonProject_Aug21/chromedriverOSX")


# Enter the website URLs
# Use <r""> to convert from normal string to raw string (used when exiting)
linkedInURL = r"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
gitHubURL = r"https://github.com/login"
faceBookURL = r"https://www.facebook.com/"
spotifyURL = r"https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F"


# Usernames and Passwords
linkedInUsername = r"<your username goes here>"
linkedInPassword = r"<your password goes here>"
linkedInPost = r"<your post goes here>"

gitHubUsername = "<your username goes here>"
gitHubPassword = "<your password goes here>"


faceBookUsername = "<your username goes here>"
faceBookPassword = "<your password goes here>"

spotifyUsername = "<your username goes here>"
spotifyPassword = "<your password goes here>"


# # #######################LINKEDIN#######################################
browser.get(linkedInURL)
browser.implicitly_wait(3)    # Wait for processing
sendUsername = browser.find_element_by_id("username")    # Found using inspect element
sendUsername.send_keys(linkedInUsername)
sendPassword = browser.find_element_by_id("password")    # Found using inspect element
sendPassword.send_keys(linkedInPassword)
logInButton = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/form/div[3]/button") # Inspect Element, click on the web object, right click on html code, copy->xpath
logInButton.click()

# enterPost = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[1]/div/div[1]/button")
# enterPost.send_keys("<postGoesHere>")
# postText = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/button/span")
# postText.click()


# # ##########################GitHUB########################
browser.execute_script("window.open('');")  # opens FB in new tab
browser.switch_to.window(browser.window_handles[1])
time.sleep(3)
browser.get(gitHubURL)
browser.implicitly_wait(3)
sendUsername = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
sendUsername.send_keys(gitHubUsername)
sendPassword = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
sendPassword.send_keys(gitHubPassword)
logInButton = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")
logInButton.click()



# # ########################FACEBOOK######################################
browser.execute_script("window.open('');")  # opens FB in new tab
browser.switch_to.window(browser.window_handles[2])
time.sleep(3)

browser.get(faceBookURL)
browser.implicitly_wait(3)
sendUsername = browser.find_element_by_id("email")
sendUsername.send_keys(faceBookUsername)
sendPassword = browser.find_element_by_id("pass")
sendPassword.send_keys(faceBookPassword)
logInButton = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
logInButton.click()



# # ########################SPOTIFY######################################
browser.execute_script("window.open('');")  # opens FB in new tab
browser.switch_to.window(browser.window_handles[3])
time.sleep(3)

browser.get(spotifyURL)
browser.implicitly_wait(3)   # Polls continuously for 3 seconds
sendUsername = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/div/input")
sendUsername.send_keys(spotifyUsername)
sendPassword = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/div/input")
sendPassword.send_keys(spotifyPassword)
logInButton = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button")
logInButton.click()
time.sleep(15)    # Slow browser so wait for 15 sec
enterSong = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/nav/ul/li[2]/a")
enterSong.click()
mySong = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/input")
mySong.send_keys("Havana")
time.sleep(10)    # Slow browser so wait a bit
playSong = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/div/div/div/section[2]/div/div[2]/div[1]/div/div/div[2]/button")
playSong.click()



#     # USE R to convert normal string to raw string, or put file path in a variable string
# Ask the websites for trust certificate so no need for webistes, chrome stores in ones place so when u log in to chrome, it automaticly bypasses all of it
# bypass/automate the authentication process with trust certificates
# have the program run from a phone instead of hard drive












