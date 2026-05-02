# workig version 2This code not uses Selenium to open Google Chrome with a 
# specific user profile and navigate to the Dino game.
import webbrowser
import pyautogui
import time
import os

# 1. Clean up the path and profile string
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Ensure 'Profile 2' matches the folder name in your User Data directory exactly
profile = "Profile 2" 

# 2. Use os.startfile for more reliable launching of internal URLs
# This bypasses webbrowser module limitations with chrome:// links
cmd = f'"{chrome_path}" --profile-directory="{profile}" chrome://dino'
os.popen(cmd)
    

# # Open the Dino game
# webbrowser.get('chrome').open("chrome://dino")
# webbrowser.get('chrome').open("chatgpt.com")


# 2. Bypass chrome:// restriction using PyAutoGUI
# Selenium can't navigate to chrome://dino directly, so we type it
print("Navigating to Dino game...")
pyautogui.hotkey('ct rl', 'l') # Focus address bar
time.sleep(0.5)
pyautogui.write('chrome://dino')
pyautogui.press('enter')   
  
print("Switching to Chrome... You have 5 seconds!")
time.sleep(5)

# 3. Simple Jump Loop
# Tip: Use 'up' instead of 'space' for slightly faster response in Dino
for i in range(10):
    pyautogui.press("space")
    print(f"Jump {i+1}")
    time.sleep(1.5) 
