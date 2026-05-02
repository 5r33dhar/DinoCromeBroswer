# DinoCromeBroswer

This script is hybrid approach to automating the Chrome Dino game. Since Chrome's security prevents Selenium from navigating directly to chrome:// URLs, using PyAutoGUI to ma
nually type the address is a solid workaround.

How Your Script FunctionsWindow Orchestration: 

1.It uses Selenium to position the browser window precisely on your screen. This is helpful if you plan to use image recognition later to "see" obstacles.

2.The "Illegal" Navigation: By using pyautogui.hotkey('ctrl', 'l'), the script tricks the browser into accepting the chrome://dino command, which Selenium’s driver.get() would normally block..---DinoCrome_selenium.py

3.Input Handling: You start with PyAutoGUI but switch to body.send_keys(Keys.SPACE). Using Selenium for the actual jumps is smarter because it sends the command directly to the browser element, making it less likely to fail if you accidentally move your mouse.
