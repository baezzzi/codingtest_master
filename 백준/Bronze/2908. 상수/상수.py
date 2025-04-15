def contrary(num1, num2) : 
    result1, result2= '', ''
    for i in range(3) :
        result1 += num1[2-i]
        result2 += num2[2-i]
    
    result1 = int(result1)
    result2 = int(result2)

    if (result1 > result2) :
        return result1
    elif (result1 < result2) :
        return result2

def __init__() :
    num1, num2 = input().split()
    result = contrary(num1, num2)
    print(result)

__init__()