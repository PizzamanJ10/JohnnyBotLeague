from time import sleep
import win32gui
import pyautogui

def moveMouse(x, y, dur):
    rect = get_client_coords()
    pyautogui.moveTo(rect[0]+x, rect[1]+y, duration=dur)


def leftClick(x = 0, y = 0, dur = 0, hold =0):
    moveMouse(x, y, dur)
    pyautogui.mouseDown(button="left")
    sleep(hold)
    pyautogui.mouseUp(button="left")


def rightClick(x = 0, y = 0, dur = 0, hold =0):
    moveMouse(x, y, dur)
    pyautogui.mouseDown(button="right")
    sleep(hold)
    pyautogui.mouseUp(button="right")


# help function
def get_client_coords():
    hwnd = win32gui.FindWindow(None, 'League of Legends')
    rect = win32gui.GetWindowRect(hwnd)
    return rect