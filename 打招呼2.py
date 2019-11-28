import time
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

time=int(time.strftime("%H"))

der=1
while der==1:
    
    bar=int(input("你有账户吗？如果没有，请输入‘1’；如果你有，请输入‘2’："))
    while bar==1:
        print("注册")
        username=input("请输入用户名：")
        password=input("请输入密码,密码只能为数字(如果不是数字可能出错)：")
        
        password2=input("请再次输入密码，密码只能为数字：")
        if password != password2:
            print("你的两次输入不一样")
            password=input("请输入密码，密码只能为数字：")
            password2=input("请再次输入密码，密码只能为数字：")
            if password == password2:
                bar=3
        elif password == password2:
            bar=3
    print("登录")
    name=input("请输入你的用户名:")
    foo=input("请输入你的密码:")
    
    if 0 <= time <7:
        temp="早上好," + name
        
    elif 7 <= time < 11:
        temp="上午好," + name
        
    elif 11 <= time < 14:
        temp="中午好," + name
        
    elif 14 <= time < 18:
        temp="下午好," + name
        
    elif 18 <= time <24:
        temp="晚上好," + name
        
    print(temp)
    speaker.Speak(temp)
    print(name,"再见")
    speaker.Speak("再见")
    der=0

