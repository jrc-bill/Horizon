#判断用户输入是否为整数，存入变量

while 1 ==1:
    print('==================================简单计算器=====================================')
    while 1 == 1:
        temp = input('请输入第一个数（整数）或 退出:')
        if temp.isdigit():
            i = int(temp)
            break
        elif temp == "退出":
            exit()
        else:
            print("您的输入不合法，请输入整数:")

#判断用户的运算符号
        
    fh=input("请输入运算符号：+:加 -:减 *:乘 /:除 //:floor除法或 退出:")
        
    if fh == "退出":
        exit()
#判断用户输入2是否为整数，存入变量
    while 1 == 1:
        temp2=input("请输入第二个数（整数）或 退出:")
        if temp2.isdigit():
            j = int(temp2)
            break
        elif temp2 == "退出":
            exit()
        else:
            print("您的输入不合法，请输入整数:")
#显示结果
    if fh == '+' :
        print("计算结果为：",i + j)
    elif fh == '-':
        print("计算结果为：",i - j)
    elif fh == '*':
        print("计算结果为：",i * j)
    elif fh == '/':
        print("计算结果为：",i / j)
    elif fh == '//':
        print("计算结果为：",i // j)
    else:
        print("您的输入有误，请重新输入(看看您的符号是不是输错了？)")
