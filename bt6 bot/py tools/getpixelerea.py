import pyautogui

print("Move the mouse to the top-left corner of the region and press Enter.")
input("Press Enter when ready...")


left, top = pyautogui.position()
print(f"Top-left corner coordinates: ({left}, {top})")

print("Move the mouse to the bottom-right corner of the region and press Enter.")
input("Press Enter when ready...")


right, bottom = pyautogui.position()
print(f"Bottom-right corner coordinates: ({right}, {bottom})")


width = right - left
height = bottom - top


print(f"Width: {width}, Height: {height}")



