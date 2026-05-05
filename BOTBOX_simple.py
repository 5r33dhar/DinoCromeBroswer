import pyautogui
import time
from PIL import ImageGrab
import numpy as np
import cv2  
import mss
import keyboard  # Faster than pyautogui for gamesimport keyboard  # Faster than pyautogui for games



def takeScreenshot():
    # Capture the screen
    #ImageW = ImageGrab.grab()
    # ImageL = ImageW.convert('L') # Convert to grayscale format
    ImageL = ImageGrab.grab().convert('L') # Convert to grayscale format
    # Display the screenshot
    #ImageW.show() 
    # Save the screenshot to a file
    #ImageW.save("ImageW.png")
    #return ImageW, ImageL
    return ImageL


def drawRectangle():
    # Define the coordinates of the rectangle (x1, y1, x2, y2)
    x1, y1, x2, y2 = 100, 100, 200, 200
    # Draw a rectangle on the screen
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=0.5)  # Drag to create a rectangle


def keyPress(key):
    # Simulate a key press (e.g., spacebar)
    pyautogui.spaceDown(key)


def CheckCollisionA(data):
    # Check for collision with an obstacle
                for i in range(665,700):
                    for j in range(290,380):
                        if data[i, j] <100:  # Assuming a threshold for obstacle detection
                            print("Collision detected!")
                        # Simulate a key press (e.g., spacebar) to jump
                        return True 
                return False


def CheckCollision(data):
   # 1. Identify the background color (Day vs Night mode)
    # We sample a pixel at (700, 200) - adjust to a clear spot in your 'sky'
    bg = data[700, 200] 
    
    # 2. Scan your detection zone
    for i in range(665, 700): # Horizontal scan
        for j in range(290, 380): # Vertical scan
            # If the pixel DOES NOT match the background, it's an obstacle
            if data[i, j] != bg:# Assuming a threshold for obstacle detection
                print("Collision detected!")
                return True
    return False




if __name__ == "__main__":
    time.sleep(3)  # Wait for 3 seconds before taking the screenshot
    print("Starting the game automation...")
    #ImageW, ImageL = takeScreenshot()
    ImageL = takeScreenshot()
    data=ImageL.load() #load the pixel data of the grayscale image
    keyboard.press('space')  # Start the game by pressing the spacebar
    while True:
        ImageL = takeScreenshot()
        data=ImageL.load()


        if CheckCollision(data):  #check for collision and jump if necessary
            pyautogui.press('space')


        # for i in range(650,700):
        #     for j in range(400,425):
        #         data[i, j] = 255  # Set the pixel at (i, j) to black (0)
        # ImageL.show()    
        # break
 
    





    #Version 3.0:            
    #     ImageL.show()       
    # print(np.asarray(ImageW))
    # ImageW.show() 
    # print('################')                        
    # print(np.asarray(ImageL)) 
    # ImageL.show()
    # print('################')
    # data=ImageL.load()
    # for i in range(650,700):
    #     for j in range(400,425):
    #         data[i, j] = 255  # Set the pixel at (i, j) to black (0)
    # ImageL.show()

    #Version 3.0: 
    # print(data)
    # print('################')
    # print(np.asarray(data))             # <class 'PixelAccess'>
    # try:
    #     print(np.array(data))
    # except NameError:
    #     print("Variable is not defined!")
    
    # print(type(data))             # <class 'int'>
    # print(isinstance(data, int))  # True
