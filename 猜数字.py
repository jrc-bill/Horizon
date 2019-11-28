import random

print("猜数字")
computer = random.randint(1,100)
player = int(input('请输入你的猜测（数字在1和100之间）：'))
der = 1
score = 0
while der == 1:
    if player != computer:
        if player > computer:
            print("大哥，大了大了！")
        if player < computer:
            print("小了小了！")
    if player == computer:
        print("恭喜你，猜对了，没有奖哦！")
        score = score + 1
        print("目前你的分数为：",score)
    player = int(input('请输入你的猜测（数字在1和100之间）：'))
