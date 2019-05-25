import os
import random
import win32gui

from util import WindowCapture
from util.MatchImg import matchImg
from util.Cursor import click_it

def loop(hwnd):
    baseImg = "../images/blackground.jpg"  # 储存的文件名  # 储存的文件名
    rect = win32gui.GetWindowRect(hwnd)
    WindowCapture.window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
    # 遍历所有图片
    for filename in os.listdir(r"../images/images-fight"):  # listdir的参数是文件夹的路径
        imagePath = "../images/images-fight/" + filename
        res = matchImg(baseImg, imagePath, 0.9)
        if res is None:
            continue
        # if filename == "exp.png":
        #     y = rect[1] - 120
        # else:
        #     continue
        #     #y = rect[1] + res["result"][1]
        # x = rect[0] + res["result"][0]
        print(filename)

        if filename == "reward.png" or filename == "finded.png":
            x = rect[0] + 20
            y = rect[1] + 560
        else:
            x = rect[0] + res["result"][0]
            y = rect[1] + res["result"][1]
        move_x = random.randint(int(x) - 2, int(x) + 2)
        move_y = random.randint(int(y) - 2, int(y) + 2)
        click_it((move_x, move_y), hwnd)
        if filename == "3.png" or filename == "4.png" or filename == "5.png" or filename == "6.png" or filename == "1.png" :
            break
