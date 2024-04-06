import time
import pyautogui


#pyautogui.FAILSAFE = True
print(pyautogui.size())

pyautogui.moveTo(100, 100, duration = 0)

pyautogui.moveRel(0, 50, duration = 1)

print(pyautogui.position())

pyautogui.click(100, 500)


#pyautogui.moveTo(1000, 1000, duration = 1)

''' 
pyautogui.moveRel(100, 0, duration = 1)
pyautogui.moveRel(0, 100, duration = 1)
pyautogui.moveRel(-100, 0, duration = 1)
pyautogui.moveRel(0, -100, duration = 1)
'''

#time.sleep(10)

pyautogui.scroll(200)

pyautogui.click(100, 100)
pyautogui.typewrite("hello Geeks !")


pyautogui.typewrite(["a", "left"])

pyautogui.hotkey("command","a")

pyautogui.hotkey("command","left")

for i in range (len("hello Geeks !a")):
    pyautogui.hotkey("delete")

