import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(currentMouseX, currentMouseY)

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
print(currentMouseX, currentMouseY)

hello = pyautogui.locateOnScreen('C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/sandbox/chrome.png', confidence=5)  # returns (left, top, width, height) of first place it is found
print(hello)