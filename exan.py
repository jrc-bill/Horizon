import random

def pretty(list):
    sum = 0
    for i in list:
        sum += i
    avg = sum / len(list)
    i = 0
    max_score = 40
    lowest = 100
    while i <len(list):
        if list[i] > max_score:
            max_score =list[i]
        if list[i] < lowest:
            lowest =list[i]
        
        i += 1
            
        
    print(' avg = {},max = {},mix = {}'.format(avg,max_score,lowest))

def main():
    stunum = 20
    list = []
    for i in range(stunum):
        list.append(random.randint(40,100))
    print(list)
    pretty(list)

if __name__ == '__main__':
    main()
    
    
        
    