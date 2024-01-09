import pyautogui
import time
import keyboard
image_found = False
mouse_speed = 0.2  # Adjust this value to control the mouse speed

# Example usage
aceandspike = [
    #((79, 213, 0), (280, 490), "3"),
    # ((79, 213, 0), (280, 630), "2"),
    ((79, 213, 0), (280, 790), "3"),

    #Right
    #((79, 213, 0), (1500, 490), "3"),
    # ((79, 213, 0), (1500, 820), "2"),
    ((79, 213, 0), (1500, 790), "3"),
]




def test_colors_and_positions_permaspike(aceandspike):
    try:
        while True:
            for target_color, position, target_name in aceandspike:
               if imagecheck():
                    #print("Exiting the loop.")
                    return  # End the loop if imagecheck returns True
               if detect_and_print(target_color, position, target_name):
                    return  # End the loop if detect_and_print returns True
         
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Testing stopped by the user.")

def color_match(color1, color2, tolerance=20):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def detect_and_print(target_color, position, target_name, tolerance=20):
    # Get the RGB color of the specified position
    pixel_color = pyautogui.pixel(position[0], position[1])

    # Check if the detected color is within the tolerance range
    if color_match(target_color, pixel_color, tolerance):
        #print(f"{target_name} - Detected color: {pixel_color}")
        print(f"{target_name} - Upgrade available ")
        keyboard.press_and_release(target_name)





def imagecheck():
    # round 11 Define the region based on the new coordinates and dimensions
    left, top, width, height = 235, 708, 184, 152
    #open left, top, width, height = 983,10 206,70
    region = (left, top, width, height)
    try:
        img = pyautogui.locateOnScreen('images/max.PNG', confidence=0.9, grayscale=True, region=region)
        if img is not None:
            print('perma upgrading done 2/0/5')
            time.sleep(0.1)
            return True  # End the loop in test_colors_and_positions
        else:
            #print('Image not found.')
            # Call your function here when the image is not found
            test_colors_and_positions_permaspike(aceandspike)
    except pyautogui.ImageNotFoundException:
        #print('Image not found. Exception caught.')
        return False


