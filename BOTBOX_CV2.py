import pyautogui
import time
from PIL import ImageGrab
import numpy as np
import cv2  # You need to install this: pip install opencv-python
import mss
import keyboard







def takeScreenshot():
    # Capture screen and convert to grayscale
    img = ImageGrab.grab()
    img_np = np.array(img) # Convert PIL to NumPy for OpenCV
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    return img_gray, img_np # Return both gray for logic and color for visual

def CheckCollision(data_gray):
    # Sample background color at (700, 200) [Your logic]
    bg = data_gray[200, 700] 
    
    collision = False
    # Scan your detection zone (665 to 700 horizontal, 290 to 380 vertical)
    for i in range(290, 380): # Vertical (y)
        for j in range(665, 700): # Horizontal (x)
            if data_gray[i, j] != bg:
                collision = True
                break
    return collision

if __name__ == "__main__":
    print("Starting in 3 seconds... Switch to Dino game!")
    time.sleep(5)
    keyboard.press('space')

    while True:
        # 1. Continuous feed capture
        gray_frame, color_frame = takeScreenshot()
        
        # 2. Collision logic using the grayscale frame
        if CheckCollision(gray_frame):
            keyboard.press('space')
            print("Jump!")

        # 3. LIVE FEED: Draw a rectangle on the color frame to see the "Jump Zone"
        # cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        cv2.rectangle(color_frame, (665, 375), (800, 425), (0, 255, 0), 2)
        cv2.rectangle(color_frame, (200, 700), (250, 750), (255, 0, 0), 3)
        
        # 4. Display the window
        # Resize it so it doesn't take up your whole screen
        small_frame = cv2.resize(color_frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Bot View - Press 'q' to Quit", small_frame)

        # 5. Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
