import win32gui

from util.HwndList import get

hwnd = get()
print(hwnd)
rect = win32gui.GetWindowRect(hwnd[0])
print(rect)