import time
import win32com.client
import pyttsx
engin = pyttsx.init()
time=int(time.strftime("%H"))
name=input("请输入你的名字:")
if 0 <= time <7:
    temp="早上"
elif 7 <= time < 11:
    temp="上午"
elif 11 <= time < 14:
    temp="中午"
elif 14 <= time < 18:
    temp="下午"
elif 18 <= time <24:
    temp="晚上"
print(temp,"好",name)
engin.say(temp,"好",name)
engin.runAndWait()
