import time
import keyboard
from pywinauto import Application


def count(current_number):
    for x in str(current_number):
        if x.isdigit():
            form.send_keystrokes(str(x))
    form.send_keystrokes("{ENTER}")
def work():
    form.send_keystrokes("{VK_MULTIPLY}")
    form.send_keystrokes("w")
    form.send_keystrokes("o")
    form.send_keystrokes("r")
    form.send_keystrokes("k")
    form.send_keystrokes("{ENTER}")

print("1 - Auto Work")
print("2 - Auto Count")
print()
ch = input("Choose one: ")
pid = input("Process ID: ")
pid = int(pid)
app = Application(backend="win32").connect(process=pid)

if ch == '1':  # Work
    number = 0
    form = app.window(title_re="🏆・vip - Discord")

    while keyboard.is_pressed("ESC") == False:
        number += 1
        work()
        print("You have work " + str(number) + " times now.")
        time.sleep(32)

elif ch == '2':  # Count

    form = app.window(title_re="📋・counting - Discord")
    number = input("Current number: ")
    number = int(number)
    current_number = int(number)

    while keyboard.is_pressed("ESC") == False:
        number += 1
        count(str(number))
        time.sleep(1.5)
