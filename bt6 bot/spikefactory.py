import pyautogui
import time
import keyboard
image_found = False
mouse_speed = 0.2  # Adjust this value to control the mouse speed

aceandspike = [
    #((79, 213, 0), (280, 490), "3"),
    # ((79, 213, 0), (280, 630), "2"),
    ((79, 213, 0), (280, 790), "3"),

    #Right
    #((79, 213, 0), (1500, 490), "3"),
    # ((79, 213, 0), (1500, 820), "2"),
    ((79, 213, 0), (1500, 790), "3"),
]

def test_colors_and_positions_spike(aceandspike):
    try:
        while True:
            for target_color, position, target_name in aceandspike:
               if imagecheck():
                    return
               if detect_and_print(target_color, position, target_name):
                    return
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Testing stopped by the user.")

def color_match(color1, color2, tolerance=20):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def detect_and_print(target_color, position, target_name, tolerance=20):
    pixel_color = pyautogui.pixel(position[0], position[1])
    # Check if the detected color is within the tolerance range
    if color_match(target_color, pixel_color, tolerance):
        imagecheck()
        time.sleep(0.1)
        print(f"{target_name} - Upgrade done")
        keyboard.press_and_release(target_name)
        time.sleep(0.1)





def imagecheck():
    try:
        img = pyautogui.locateOnScreen('images/spike.PNG', confidence=0.9, grayscale=True)
        if img is not None:
            print('Upgrading done spike 2/0/4')
            # pyautogui.moveTo(x=760, y=230, duration=mouse_speed)
            # pyautogui.click()
            print('Finished upgrading spike factory 2/0/3')
            time.sleep(0.1)
            return True  # End the loop in test_colors_and_positions
        else:
            #print('Image not found.')
            test_colors_and_positions_spike(aceandspike)
    except pyautogui.ImageNotFoundException:

        return False

