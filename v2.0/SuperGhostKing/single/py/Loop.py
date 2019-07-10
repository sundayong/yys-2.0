import os
import random
import time
import win32gui
from util import WindowCapture
from util.MatchImg import matchImg
from util.Cursor import click_it


def loop(hwnd):
    # print("线程开始执行："+hwnd)
    # while True:
        baseImg = "../images/blackground.jpg"  # 储存的文件名  # 储存的文件名
        rect = win32gui.GetWindowRect(hwnd)
        WindowCapture.window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        # 遍历所有图片
        for filename in os.listdir(r"../images/images-fight"):  # listdir的参数是文件夹的路径
            imagePath = "../images/images-fight/" + filename
            res = matchImg(baseImg, imagePath, 0.99)
            # print("==================:" + filename)
            if res is None:
                continue
            print(time.ctime()+" "+ filename)
            #疲劳值满之后，暂停100分钟
            if filename == "end.png":
                print(time.ctime()+" 进入休眠....")
                time.sleep(1800)
                print(time.ctime()+" 休眠完成，继续...")
                x1 = rect[0] + 837
                y1 = rect[1] + 207
                move_x1 = random.randint(int(x1) - 2, int(x1) + 2)
                move_y1 = random.randint(int(y1) - 2, int(y1) + 2)
                click_it((move_x1, move_y1), hwnd)
            if filename == "00.png":
                print(time.ctime()+" 发现鬼王.......")
                x1 = rect[0] + 938
                y1 = rect[1] + 140
                move_x1 = random.randint(int(x1) - 2, int(x1) + 2)
                move_y1 = random.randint(int(y1) - 2, int(y1) + 2)
                click_it((move_x1, move_y1), hwnd)
            if filename == "reward.png":
                x = rect[0] + 20
                y = rect[1] + 560
            else:
                x = rect[0] + res["result"][0]
                y = rect[1] + res["result"][1]
            move_x = random.randint(int(x) - 2, int(x) + 2)
            move_y = random.randint(int(y) - 2, int(y) + 2)
            click_it((move_x, move_y), hwnd)
