import sys
import time

from SuperGhostKing.single.py.Loop import loop
from util.HwndList import get
import threading


def main():
    print("欢迎来到阴阳师联盟！")
    arg = 0
    tt = 2
    # if sys.argv.__len__() > 1:  #多人组队
    #     arg = sys.argv[1]
    # else:
    #     tt = 1
    #获取所有阴阳师句柄 
    list = get()
    while True:
        time.sleep(tt)  # 设置隔2秒运行一次

        #循环所有句柄
        for hd in list:
            loop(hd)
        # threading.Thread(target=loop, args=hd).start()

if __name__=="__main__":
    main()






