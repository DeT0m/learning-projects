#!usr/bin/env python3

import pyautogui

pyautogui.PAUSE = 10  # Defining 10 second pause between moves

try:
    # Move cursor 1 pixel one of four ways each 10 seconds
    while True:
        pyautogui.move(1, 0)
        pyautogui.move(0, 1)
        pyautogui.move(-1, 0)
        pyautogui.move(0, -1)
except KeyboardInterrupt:  # Exit program
    print('Stopped.')
