import pyautogui
import time
import keyboard
image_found = False
mouse_speed = 0.2  # Adjust this value to control the mouse speed


def imagecheck():
    # Round 11: Define the region based on the new coordinates and dimensions
    left, top, width, height = 1724, 880, 182, 199
    region = (left, top, width, height)
    
    while True:
        try:
            img = pyautogui.locateOnScreen('images/speedtrue.PNG', confidence=0.9, grayscale=True, region=region)
            if img is not None:
                print('speed is true')
                keyboard.press_and_release('space')
                time.sleep(1)

                # You can perform additional actions here if needed
                return True  # End the loop or function
        except pyautogui.ImageNotFoundException:
            pass  # Image not found, continue the loop
        time.sleep(0.1)  # Adjust the sleep duration as needed

# Call the function
imagecheck()
