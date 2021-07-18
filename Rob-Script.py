import time
import keyboard
import pyperclip
import pyautogui, sys


def GetID():
    x, y = pyautogui.position()
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')
    keyboard.press_and_release('up')
    keyboard.press_and_release('enter')

def CopyClipboard():
    clipboard = pyperclip.paste()
    pyperclip.copy(clipboard)
    return clipboard


while keyboard.is_pressed("ESC") == False:

    keyboard.wait("down")

    if keyboard.is_pressed("down"):
        time.sleep(0.1)
        clipboard = str(CopyClipboard())
        keyboard.write("*rob " + clipboard)
        keyboard.press_and_release("enter")
