import pyautogui
import keyboard
from PIL import ImageGrab

def capture_cursor_position():
    # Get the current cursor position
    x, y = pyautogui.position()
    return x, y

def capture_rgb_values(x, y):
    # Capture the screen and get the RGB values of the pixel at the specified position
    screenshot = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    pixel_rgb = screenshot.getpixel((0, 0))
    return pixel_rgb

# Start the loop to continuously check for Enter key press
while True:
    try:
        if keyboard.is_pressed("enter"):
            # Capture cursor position
            position = capture_cursor_position()
            
            # Capture and print RGB values
            rgb_values = capture_rgb_values(*position)
            print(f"Cursor position: x={position[0]}, y={position[1]}, RGB={rgb_values}")

            # Add a delay to prevent multiple captures for a single key press
            keyboard.wait("enter")
    except KeyboardInterrupt:
        # Exit the loop if KeyboardInterrupt (e.g., when you press Ctrl+C)
        break
#Cursor position: x=1663, y=26, RGB=(49, 39, 24)
#Cursor position: x=1659, y=12, RGB=(193, 153, 96)
    

    

