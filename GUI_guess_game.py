import random, easygui

# secret = random.randint(1,10) # 生成1-10的随机整数
secret = 7
tries = 0
easygui.msgbox("""AHOY!!! 你现在有3次机会，在1-10内猜一个整数。
千万不要掉以轻心，因为失败者将会永远成为Single Dog!""")

guess = easygui.integerbox("请输入命运数字：", lowerbound=1, upperbound=10)
tries += 1

while tries <3 and guess != secret:
    easygui.msgbox("错啦！哈哈！")
    chances = 3 - tries
    guess = easygui.integerbox("注意，你还有 %d 次机会，请再次输入命运数字：" % chances, lowerbound=1, upperbound=10)
    tries += 1

if guess == secret:
    easygui.msgbox("呵，竟然让你猜对了！")
else:
    easygui.msgbox("Single dog, Single dog, single all the way~ Bye Bye!")