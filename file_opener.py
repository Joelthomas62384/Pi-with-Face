import pyautogui
from time import sleep

def openfile(name):
    pyautogui.press('win')
    sleep(2)
    pyautogui.typewrite(name)
    sleep(2)
    pyautogui.press("ENTER")