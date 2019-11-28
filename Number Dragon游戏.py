from random import *
import time
J = 11
Q = 12
K = 13
A = 1
pk_list = [3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2]
readyToOut = None


def computer_output():
    time1 = 0
    readyToOut = -1
    if int(lastOutPut) == -1:
        if state == 0:
            for i in playerList:
                if i - 1 in computerList:
                    readyToOut = i-1
                else:
                    computerList[0] = max(playerList) - 1
                    readyToOut = computerList[0]
        else:
            readyToOut = choice(computerList)

    else:
        if int(lastOutPut) + 1 in computerList:
            readyToOut = int(lastOutPut) + 1
        elif state == 1:
            if 2 in computerList:
                readyToOut = 2
        else:
            readyToOut = "不出"
    if state == 1:
        if readyToOut != -1:
            if time1 == 3:
                computerList.append(choice(pk_list))
                time1 = 0
    if readyToOut == -1:
        readyToOut = "不出"
    if readyToOut != "不出":
        computerList.pop(int(computerList.index(readyToOut)))
    time1 += 1
    return readyToOut


def player_output():
    time2 = 0
    readyToOut = -1
    print("你有{}这些牌".format(playerList))
    if lastOutPut + 1 in playerList:
        correct = True
    elif 2 in playerList:
        correct = True
    elif lastOutPut == -1:
        correct = True
    elif lastOutPut == 2:
        input("你无牌可出，只能输入no")
        time.sleep(1)
        readyToOut = -1
        correct = False
    else:
        input("你无牌可出，只能输入no")
        time.sleep(1)
        readyToOut = -1
        correct = False

    while correct:
        readyToOut = input('请输入你要出的牌（输入数字或no）')

        if readyToOut.isalpha():
            readyToOut = -1
            break
        if int(readyToOut) not in playerList:
            continue
        if int(readyToOut) == 2:
            break
        if max(playerList) < int(readyToOut):
            continue
        if lastOutPut != -1:
            if int(readyToOut) == lastOutPut + 1:
                break
            else:
                continue
        else:
            break

    if  readyToOut != -1:
        playerList.remove(int(readyToOut))
    if time2 == 1:
        playerList.append(choice(pk_list))
    return readyToOut



print('欢迎来到ND战场')
print('''机器有七张牌，你有六张
      下家只能接上家的牌
      2能压过所有牌''')
time.sleep(1)



while True:

    computerList = sample(pk_list, 7)
    playerList = sample(pk_list, 6)
    state = 0
    lastOutPut = -1

    while True:
        comOut = computer_output()

        if comOut != "不出":

            print("机器出了{}".format(comOut))
            lastOutPut = comOut
            if comOut == 2:
                print("机器出了最大的！")
                time.sleep(1)
        else:
            print("机器不出")
            time.sleep(1)
            lastOutPut = -1
        if len(computerList) == 0:
            break

        time.sleep(1)
        print("机器剩下{}张牌".format(len(computerList)))
        time.sleep(1)
        state = 1
        comOut = player_output()
        if comOut != -1:

            print("你出了{}".format(comOut))
            time.sleep(1)
            if comOut == 2:
                print("你出了最大的！")
                time.sleep(1)
            lastOutPut = comOut
        else:
            print("你不出")
            time.sleep(1)
            lastOutPut = -1
        if len(playerList) == 0:
            break

    if len(computerList) == 0:
        print("机器赢了！")
        time.sleep(1)
    else:
        print("你赢了！")
        time.sleep(1)
    input("输入任意字符并回车以继续：")






