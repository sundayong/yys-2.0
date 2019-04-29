import time

from eat.py.Loop import loop
from util.HwndList import get


def main():
    print("欢迎来到痒痒鼠！")
    arg = 0
    tt = 5
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

if __name__=="__main__":
    main()






