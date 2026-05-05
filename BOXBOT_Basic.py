import pyautogui
import time
from PIL import ImageGrab
import numpy as np



def takeScreenshot():
    # Capture the screen
    ImageW = ImageGrab.grab()
    ImageL = ImageW.convert('L') # Convert to grayscale format
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


def CheckCollision(data):
    # Check for collision with an obstacle
                for i in range(665,700):
                    for j in range(290,380):
                        if data[i, j] <100:  # Assuming a threshold for obstacle detection
                            print("Collision detected!")
                        # Simulate a key press (e.g., spacebar) to jump
                        return True 
                return False






if __name__ == "__main__":
    time.sleep(3)  # Wait for 3 seconds before taking the screenshot
    print("Starting the game automation...")
    #ImageW, ImageL = takeScreenshot()
    ImageL = takeScreenshot()
    data=ImageL.load() #load the pixel data of the grayscale image
    pyautogui.press('space')  # Start the game by pressing the spacebar
    while True:
        ImageL = ImageL.convert('L')
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
