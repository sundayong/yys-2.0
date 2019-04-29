import os
import random
import time
import win32gui
from util import WindowCapture
from util.MatchImg import matchImg
from util.Cursor import click_it


# 刷本线程T2，当T1执行的时候T2等待
def loop(hwnd, baseImgPath, imageDirPath):
    baseImg = baseImgPath  # 储存的文件名
    rect = win32gui.GetWindowRect(hwnd)
    WindowCapture.window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
    # 遍历所有图片
    for filename in os.listdir(imageDirPath):  # listdir的参数是文件夹的路径
        imagePath = "../images/images-fight/" + filename
        res = matchImg(baseImg, imagePath, 0.7)
        if res is None:
            continue
        print(filename)
        print(res)
        if filename == "reward.png":
            x = rect[0] + 20
            y = rect[1] + 560
        else:
            x = rect[0] + res["result"][0]
            y = rect[1] + res["result"][1]
        move_x = random.randint(int(x) - 2, int(x) + 2)
        move_y = random.randint(int(y) - 2, int(y) + 2)
        print(move_x, move_y)
        click_it((move_x, move_y), hwnd)
