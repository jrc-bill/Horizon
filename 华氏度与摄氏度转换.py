#coding=utf-8


def c_f(num):
    answer = (num - 32) / 1.8
    return answer


def f_c(num):
    answer = num*1.8 + 32
    return answer
while True:

    state = int(input('请选择方向，1为华氏度转摄氏度，2为摄氏度转华氏度：'))

    num = int(input('请输入要转换的数字：'))
    if state == 1:
        hh = c_f(num)
        print("结果是{}C°".format(round(hh, 1)))
    elif state == 2:
        hh = f_c(num)
        print("结果是{}F°".format(hh))