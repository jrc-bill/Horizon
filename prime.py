
def prime(num):

    if num % 2 == 0 and num != 2:
        return False
    elif num % 3 == 0 and num != 3:
        return False
    elif num % 5 == 0 and num != 5:
        return False
    elif num % 7 == 0 and num != 7:
        return False

    i = num - 1
    while i >1  :
        if num % i == 0:
            return False
        i -= 1
    return True
while True:
    ip =  int(input("type a number:"))

    s = prime(ip)

    if s:
        print("it's a prime")

    else:
        print("it isn't a prime")