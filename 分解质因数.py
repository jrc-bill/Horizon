num = int(input("请输入待分解的正整数："))


def f1(num):
    list = []
    i = 1
    state = 0
    while i <= num:
        if num % i == 0:
            val = num / i
            num = num / i
            list.append(num)
            state = 1
        if state == 0:
            i += 1
    print (list)


f1(num)
