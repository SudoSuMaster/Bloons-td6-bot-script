import pyautogui
import time
import keyboard

# upgrade 1
def color_match(color1, color2, tolerance=20):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def detect_and_print(target_color, position, tolerance=20):
    # Get the RGB color of the specified position
    pixel_color = pyautogui.pixel(position[0], position[1])

    # Check if the detected color is within the tolerance range
    if color_match(target_color, pixel_color, tolerance):
        print(f"Detected color: {pixel_color}")
        print("Color matches the specified color.")
        keyboard.press_and_release('1')
        time.sleep(0.1)
    else:
        print(f"Detected color: {pixel_color}")
        print("Color does not match the specified color.")


target_color = (79, 213, 0)  # Example: RGB values with some tolerance
specified_position = (1474, 490)  # Example: (x, y) coordinates

# Run the loop for testing
try:
    while True:
        detect_and_print(target_color, specified_position)
        time.sleep(0.1)  # Adjust the sleep duration as needed
except KeyboardInterrupt:
    print("Testing stopped by the user.")
