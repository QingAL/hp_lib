import os
import time
import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        posStr = "鼠标位置:"+"x:"+str(x).rjust(4)+' '+'y:'+str(y).rjust(4)
        print(posStr)   # 打印坐标
        time.sleep(1)
        os.system('cls')    # 清除屏幕
except KeyboardInterrupt:
    print("end")
