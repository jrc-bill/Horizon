print("分数转换器")

while 1 == 1:
    score=int(input("请输入100分制的分数:"))
    if score > 100 or score<0:
        print("请输入0与100之间的数！请重新输入")
        continue
    elif 90 <= score <= 100:
        dd = "A，不错，继续保持！"
    elif  80 <= score < 90 :
        dd = "B，还行，再加把劲！"
    elif 60 <= score < 80:
        dd = "C，一般，要努力哟！"
    elif score < 60:
        dd = "D，较差，看看哪里出了问题吧！"
    elif score > 100:
        print("你的输入不合法，请重新输入")
    print("您的等第为" , dd)      
        
