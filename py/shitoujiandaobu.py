import random
import time
from Module.InputValue import input_value as inp
punches = ('石头', '剪刀', '布')
win_msg = ("平局", "玩家胜", "电脑胜")
input_msg = "石头：0，剪刀：1，布：2，请出拳："
error_msg = "输入有误，请重新出拳"

def user_choice():
    while True:
        choice = inp(input_msg, error_msg)
        if choice != 0 and choice != 1 and choice != 2:
            print(error_msg)
            continue
        return choice

# 一次对决，返回值 0：平局，1：玩家胜，2：电脑胜
def Duel():
    computer_cho = random.randint(0, 2)
    user_cho     = user_choice()
    win = None
    if user_cho == computer_cho:
        win = 0
    # elif (user_cho < computer_cho and abs(user_cho-computer_cho) == 1
    #    or user_cho > computer_cho and abs(user_cho-computer_cho) == 2):
    #     win = 1
    elif punches[user_cho] == punches[computer_cho-1]: #因为list[-1]取倒数第一个，user出布，电脑出石头时，punches[computer_cho-1]取布
        win = 1
    else :
        win = 2
    print("电脑出拳：{}".format(punches[computer_cho]))
    print("玩家出拳：{}".format(punches[user_cho]))
    print(win_msg[win])
    return win

def Game() :
    number = inp("请设定局数：", "错误！请输入数字")
    if number < 1 : print("不玩了！") ; return
    user_point = 0
    computer_point = 0
    for i in range(1,number+1) :
        print("{0:*^20}".format("第%d局" % i))
        result = Duel()
        if result == 1 : user_point += 1
        elif result == 2 : computer_point += 1

    print("{0:*^20}".format("最终结果"))
    time.sleep(2.0)
    if user_point > computer_point :
        print("玩家胜！！！")
    elif user_point < computer_point :
        print("电脑胜( ╯□╰ )")
    else :
        print("平局。。。")

Game()