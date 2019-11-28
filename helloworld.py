import time
lastOutPut = int(input())
playerList = [1,2,3,4,5]
print(max(playerList))
def player_output():
    readyToOut = -1
    print("你有{}这些牌".format(playerList))

    if lastOutPut + 1 in playerList:
        correct = True
    elif lastOutPut == -1:
        correct = True
    else:
        print("你无牌可出。")
        readyToOut = -1
        time.sleep(1)
    while correct:
        readyToOut = input('请输入你要出的牌（输入数字或no）')

        if readyToOut.isalpha():
            readyToOut = -1
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
    return readyToOut
print(player_output())