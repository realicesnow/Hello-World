# coding=utf-8
import random
# 获胜次数
win_times = 0
while win_times <= 2:
    player = input('请输入：剪刀(0)  石头(1)  布(2):')
    player = int(player)
    computer = random.randint(0, 2)

    if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or ((player == 2) and (computer == 1)):
        win_times += 1
        print('获胜，哈哈，你太厉害了')
    elif player == computer:
        print('平局，要不再来一局')
    else:
        print('输了，不要走，洗洗手接着来，决战到天亮')
