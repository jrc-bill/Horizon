def save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(file,'a')
    file.write(data)
up = []
dl = []
        
username = []
password = []
up = []
while True:
        while True:
            is_not = input("您是否有账号？如果没有：请输入 1注册 如果有了，请输入2 登录 或输入“退出”以退出：")
            if is_not == "1" or "2":
                break
            elif is_not == "退出":
                exit()
            else:
                print("您的输入不合法：请输入“1”以注册 或输入2 以登录")
        while is_not == "1":
            
            while is_not == "1":
                un=input("注册账号：请输入用户名（用户名不能全部输入数字哦）：")
                if un.isdigit():
                    print("用户名不能全部输入数字哦")
                else:
                    break

            username.extend([un])
            while True:
                pw1 = (input ("注册账号：请输入密码(需全部为数字,6位以上)："))
                if len(pw1) >= 1 and pw1.isdigit():
                    pw11 = pw1
                    break
                else:
                    print("您的密码输入不合法，请重新输入")
                
            while True:
                pw2 = (input ("注册账号：请再次输入密码(需全部为数字，6位以上):"))
                if len(pw2) >= 1 and pw2.isdigit():
                    pw22 = pw2
                    break
                else:
                    print("您的密码输入不合法，请重新输入")


            if pw11 == pw22 :
                  password.append(pw11)
                  is_not = "2"
                  break
            else:
                print("您的两次输入不同，请重新输入")
        up.append(username+password)
        while is_not == "2":
            while is_not == "2":
                username2 = input("请输入用户名,如果没有账号，请输入 1 以返回开始界面 或 “退出”以退出:")
                if username2 == "1":
                    is_not = "1"
                elif username2 == "退出":
                    exit()
                else:
                    break
                    
            while is_not == "2" :
                password2 = input("请输入密码,如果没有账号，请输入 1 以返回开始界面 或 “退出”以退出:")
                if password2 == "1":
                    is_not = "1"
                elif password2 == "退出":
                    exit()
                else:
                    break
            dl.append(username2 + password2)
            print(dl,up)
            while is_not == "2":
                if dl in up:
                    print("登录成功")
                    break
                else:
                    spam2=input("密码出错了！请输入“0”以重新输入 或输入 1 以返回开始界面 或 “退出”以退出:")
                    if spam2 == "1":
                        is_not = "1"
                    elif spam2 == "0":
                        continue
                    elif spam2 == "退出":
                        exit()
                    
        break
print("hello,",username2)
print(dl)
          
          
