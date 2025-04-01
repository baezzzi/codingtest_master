number = [i for i in range (1, 31)]

def deleteNum(num) :
    if (num in number) :
        number.remove(num)
    
    return 0

def __init__() :
    for i in range(28) :
        num = int(input())
        deleteNum(num)
    
    number.sort()
    print(number[0])
    print(number[1])

__init__()