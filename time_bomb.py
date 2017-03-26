import time
import easygui

seconds = easygui.integerbox("请设定爆炸倒计时（s）：")
for i in range(seconds,0,-1):
    print("%ds后将会爆炸！"%i + "*"*i)
    time.sleep(1)
easygui.msgbox("BLAST OFF!")