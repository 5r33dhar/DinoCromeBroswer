# This script uses Selenium to open the Chrome Dinosaur game and
#  PyAutoGUI to simulate key presses.
# It opens Chrome, navigates to the Dino game, and sends space key presses 
# to make the dinosaur jump.
# Note: Selenium cannot navigate to chrome://dino directly, 
# so we use PyAutoGUI to type the URL and press Enter.

import os
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

driver = webdriver.Chrome()
# Initialize the Chrome WebDriver (make sure chromedriver is in your PATH)
urls = r"chrome://dino"
#driver.get("chrome://dino");
# # Open the Chrome Dinosaur game in the browser
try:
    driver.get(urls)
except:
    # Ignore the "Internet Disconnected" error 
    # because that's exactly what we want for the Dino game!
    pass

time.sleep(5)
pyautogui.press('space')
time.sleep(10)# Wait for user to switch to Chrome window

#Simple jump loop
for i in range(10):
    pyautogui.press("space")   # or use "up" for faster response
    print(f"Jump {i+1}")
    time.sleep(1.5)
         
