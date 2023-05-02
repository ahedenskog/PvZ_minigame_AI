import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

minigame = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/minigameBtn.png", confidence=0.9)
if minigame != None:
    pyautogui.click(minigame)

Whacky = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/whack-a-zombie/WAZ.PNG", confidence=0.9)
if Whacky != None:
    pyautogui.click(Whacky)

NewGame = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/whack-a-zombie/newGame1.PNG", confidence=0.9)
if NewGame != None:
    pyautogui.click(NewGame)

Confirm = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/whack-a-zombie/newGame2.PNG", confidence=0.9)
if Confirm != None:
    pyautogui.click(Confirm)

while True:
    Zombie = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/zombie.png", confidence=0.6)
    Buckethead = pyautogui.locateOnScreen("C:/Users/albin.hedenskog/Documents/GitHub/PvZ_minigame_AI/assets/buckethead.png", confidence=0.6)
    if Zombie != None:
        print("I see a zombie at:", Zombie)
        pyautogui.click(Zombie)
    else:
        print("I'm looking for zombies...")  
    # if Buckethead != None:
    #      print("I see a buckethead at:", Buckethead)    
    #      pyautogui.click(Buckethead)
