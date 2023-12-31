import pyautogui
import time
import keyboard

# Example usage
targets_and_positions = [
    #Left
    ((79, 213, 0), (280, 490), "1"),
    # ((79, 213, 0), (280, 630), "2"),
    ((79, 213, 0), (280, 790), "3"),

    #Right
    ((79, 213, 0), (1500, 490), "1"),
    # ((79, 213, 0), (1500, 820), "2"),
    ((79, 213, 0), (1500, 790), "3"),
]

def color_match(color1, color2, tolerance=20):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def detect_and_print(target_color, position, target_name, tolerance=20):
    # Get the RGB color of the specified position 
    pixel_color = pyautogui.pixel(position[0], position[1])

    # Check if the detected color is within the tolerance range
    if color_match(target_color, pixel_color, tolerance):
        print(f"{target_name} - Detected color: {pixel_color}")
        print(f"{target_name} - Upgrade available ")
        keyboard.press_and_release(target_name)
        time.sleep(0.1)
    else:
        print(f"{target_name} - Detected color: {pixel_color}")
        print(f"{target_name} - Cannot upgrade")

def test_colors_and_positions(targets_and_positions):
    try:
        while True:
            for target_color, position, target_name in targets_and_positions:
                detect_and_print(target_color, position, target_name)
            time.sleep(0.1)  # Adjust the sleep duration as needed
    except KeyboardInterrupt:
        print("Testing stopped by the user.")

# Run the test function
test_colors_and_positions(targets_and_positions)
