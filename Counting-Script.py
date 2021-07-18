import time
import keyboard

while True:

    current = input("Current: ")

    if current.isdigit():
        break
    else:
        print("Sorry, something went wrong. Try again.")

current = int(current)
number = current
member = 1

while keyboard.is_pressed("ESC") == False:

    if keyboard.is_pressed('8'):
        # PLUS
        time.sleep(0.1)
        number = number + member
        keyboard.press_and_release('ctrl + a + del')
        keyboard.write("Current Number: " + str(number) + "        ")
    if keyboard.is_pressed('5'):
        # TYPE
        time.sleep(0.1)
        number = number + member
        keyboard.press_and_release('ctrl + a + del')
        keyboard.write(str(number - 1))
        keyboard.press_and_release('enter')
    if keyboard.is_pressed('2'):
        # MINUS
        time.sleep(0.1)
        number = number - member
        keyboard.press_and_release('ctrl + a + del')
        keyboard.write("Current Number: " + str(number) + "        ")

    if keyboard.is_pressed('9'):
        # TYPE
        time.sleep(0.1)
        keyboard.press_and_release('ctrl + a + del')
        keyboard.write('PAKYU CARL @Carl-bot#1536')
        keyboard.press_and_release('enter')
    if keyboard.is_pressed('7'):
        # TYPE
        time.sleep(0.1)
        keyboard.press_and_release('ctrl + a + del')
        keyboard.write('>join')
        keyboard.press_and_release('enter')
