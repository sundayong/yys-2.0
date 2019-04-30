import sys
import time

from Buzhihuo.single.py.Loop import loop
from util.HwndList import get


def main():
    print("欢迎来到阴阳师联盟！")
    arg = 0
    tt = 0.00
    #获取所有阴阳师句柄
    list = get()
    while True:
        # time.sleep(tt)  # 设置隔2秒运行一次

        #循环所有句柄
        for hd in list:
            loop(hd)

if __name__=="__main__":
    main()






