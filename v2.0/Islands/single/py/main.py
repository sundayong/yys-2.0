import os
import random
import threading
import time

import win32gui

from util import WindowCapture
from util.Cursor import click_it
from util.HwndList import get
from util.MatchImg import matchImg


# 每四十分钟执行一次，执行的时候其它线程等待
def shower_job(remberTime):
    print("洗澡线程开始执行......")
    print("Start : %s" % time.ctime())
    loop_2(hwnd)
    print("End : %s" % time.ctime())


# 定时40分钟
def remberTime_job():
    print("定时线程开始执行......")
    print("Start : %s" % time.ctime())
    time.sleep(2400)
    print("End : %s" % time.ctime())


def fight_job():
    loop(hwnd)


# 刷本线程T2，当T1执行的时候T2等待
def loop(hwnd, baseImgPath="../images/background.jpg", imageDirPath="../images/images-fight/"):
    global Flag
    Flag = True
    while Flag:
        time.sleep(1)
        print("刷本线程正在执行......")
        baseImg = baseImgPath  # 储存的文件名
        rect = win32gui.GetWindowRect(hwnd)
        WindowCapture.window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        # 遍历所有图片
        for filename in os.listdir(imageDirPath):  # listdir的参数是文件夹的路径
            imagePath = imageDirPath + filename
            res = matchImg(baseImg, imagePath, 0.7)
            if res is None:
                continue
            print(filename)
            print(res)
            if filename == "end.png":
                print("刷本线程停止执行......")
                return
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
    print("刷本线程停止执行......")
    return


def loop_1(hwnd, baseImgPath="../images/background1.jpg", imageDirPath="../images/base/"):
    while True:
        time.sleep(1)
        print("恢复初始界面线程正在执行......")
        baseImg = baseImgPath  # 储存的文件名
        rect = win32gui.GetWindowRect(hwnd)
        WindowCapture.window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        # 遍历所有图片
        for filename in os.listdir(imageDirPath):  # listdir的参数是文件夹的路径
            imagePath = imageDirPath + filename
            res = matchImg(baseImg, imagePath, 0.7)
            if res is None:
                continue
            # 判断是否已经退出到初始界面
            if filename == "zaotang.png":
                print("恢复初始界面线程停止执行......")
                return
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
    print("恢复初始界面线程停止执行......")


def loop_2(hwnd, baseImgPath="../images/background2.jpg", imageDirPath="../images/shower/"):
    while True:
        time.sleep(1)
        print("洗澡线程正在执行......")
        baseImg = baseImgPath  # 储存的文件名
        rect = win32gui.GetWindowRect(hwnd)
        WindowCapture.window_capture(baseImg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        # 遍历所有图片
        for filename in os.listdir(imageDirPath):  # listdir的参数是文件夹的路径
            imagePath = imageDirPath + filename
            res = matchImg(baseImg, imagePath, 0.7)
            if res is None:
                continue
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
            # 判断是否洗完澡
            if filename == "reward.png":
                print("洗澡线程停止执行......")
                return
    print("洗澡线程停止执行......")
    return


hd = get()
hwnd = hd[0]


def currentThread_job():
    while True:
        time.sleep(2)
        print("当前活跃线程:" + time.ctime(), end="")
        print(threading.enumerate())


def main():
    Flag = True
    threading.Thread(target=currentThread_job, name="currentThread").start()
    while True:
        remberTime = threading.Thread(target=remberTime_job, name="remberTime")
        shower = threading.Thread(target=shower_job, args=(remberTime), name="shower")
        fight = threading.Thread(target=fight_job, name="fight")
        # 启动定时线程
        remberTime.start()
        # 启动刷本线程一直执行
        fight.start()

        # 等待定时线程remberTime执行完
        remberTime.join()
        # 执行主线程代码
        # 1.停止刷本线程fight 2.将界面恢复至初始界面
        Flag = False
        loop_1(hwnd)

        # 启动洗澡线程，等定时线程执行完执行
        shower.start()
        # 等待洗澡线程执行完
        shower.join()
        # 执行主线程代码回到主界面
        loop_1(hwnd)


if __name__ == "__main__":
    main()
