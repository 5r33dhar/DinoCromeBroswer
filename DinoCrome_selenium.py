# working version 1 using Selenium to open Chrome and 
# send keys directly to the browser, which should be more 
# reliable than PyAutoGUI for this purpose. 
# The code opens Chrome, navigates to the Dino game, and sends space key 
# presses to make the dinosaur jump.

import time
import pyautogui
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 1. Start Selenium
driver = webdriver.Chrome()
driver.maximize_window()
driver.minimize_window()
driver.set_window_size(600, 900)
driver.set_window_position(1273, 46)

# Get the current window position as a dictionary
position = driver.get_window_position()

# Access individual coordinates
x = position.get('x')
y = position.get('y')
print(f"Window is at X: {x}, Y: {y}")


# 2. Bypass chrome:// restriction using PyAutoGUI
# Selenium can't navigate to chrome://dino directly, so we type it
print("Navigating to Dino game...")
pyautogui.hotkey('ctrl', 'l') # Focus address bar
time.sleep(0.5)
pyautogui.write('chrome://dino')
pyautogui.press('enter')

# 3. Wait for game to load
time.sleep(3)
body = driver.find_element(By.TAG_NAME, "body")

# 4. Simple jump loop
print("Starting the jump loop!")
# Press space once to start the game
body.send_keys(Keys.SPACE)

# Now we can use Selenium to send keys directly to the browser, 
# which should be more reliable than PyAutoGUI for this purpose.
for i in range(10):#
    body.send_keys(Keys.SPACE) # Use Selenium keys for better focus
    print(f"Jump {i+1}")
    time.sleep(1.5)

#############    

# Optional: Keep browser open for a bit before closing
time.sleep(5)

# Get the current window rectangle (position and size)
rect = driver.get_window_rect()
# Print the current window rectangle (position and size)
print(rect) 

time.sleep(5)

driver.quit()
