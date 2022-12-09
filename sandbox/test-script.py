import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

oi = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/sandbox/chrom.PNG", confidence=0.6)
pyautogui.click(oi)
pyautogui.keyDown('ctrl')
pyautogui.press('t')
pyautogui.keyUp('ctrl')
pyautogui.typewrite('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
pyautogui.press('enter')