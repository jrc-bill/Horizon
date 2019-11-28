from random import randint

import time
print("Rule of Craps 游戏规则：")
rule = [
'玩家第一次摇骰子如果摇出了7点或11点，玩家胜；',
'玩家第一次如果摇出2点、3点或12点，庄家胜；',
'其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；',
'如果玩家摇出了第一次摇的点数，玩家胜；'
'其他点数，玩家继续要骰子，直到分出胜负。'
]
for i in rule:
    print(i)
    time.sleep(0.1)

money = 1000
times = 0
while money > 0:

    if times == 4:
        money += 500
        print("四局结束，你获得500元")
        times = 0
    print("你有{}元钱".format(money))
    goon = False
    while True:
        dept = input("请下注(all为全压)：")
        if dept == 'all':
            dept = money
        else:
            dept = int(dept)
        if 0 < dept <= money:
            break
    print("您下了{}元赌注".format(dept))
    first = randint(1,6) + randint(1,6)
    print("你的第1次点数为 :{}".format(first))
    time.sleep(0.5)
    if first == 7 or first == 11:
        print("你赢了!")
        money += dept
    elif first == 2 or first == 3 or first ==11:
        print("庄家赢了!")
        money -= dept
    else:
        goon = True
        ts =2
    while goon:
        goon = False
        second = randint(1,6)+randint(1,6)
        time.sleep(1)
        print("你的第{}次点数为:{}".format(ts,second))

        if second == 7:
            print("点数为7! 庄家赢了！!")
            money -= dept
        elif second == first:
            print("点数相同! 你赢了!")
            money += dept
        else:
            goon = True
            ts += 1
    times = times + 1
print("你破产了，再见")
