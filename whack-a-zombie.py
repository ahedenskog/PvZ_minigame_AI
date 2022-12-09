import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

minigame = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/minigameBtn.png", confidence=0.9)
pyautogui.click(minigame)

Whacky = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/whack-a-zombie/WAZ.PNG", confidence=0.9)
pyautogui.click(Whacky)

NewGame = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/whack-a-zombie/newGame1.PNG", confidence=0.9)
pyautogui.click(NewGame)

Confirm = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/whack-a-zombie/newGame2.PNG", confidence=0.9)
pyautogui.click(Confirm)