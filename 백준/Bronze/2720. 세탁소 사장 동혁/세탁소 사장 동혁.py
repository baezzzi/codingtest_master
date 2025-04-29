## 2720 세탁소 사장 동혁

def __init__() :
    case = int(input())
    quarter, dime, nickel, penny = 0, 0, 0, 0
    result = []

    for _ in range(case) :
        C = int(input())
        quarter, C = divmod(C, 25)
        dime, C = divmod(C, 10)
        nickel, C = divmod(C, 5)
        penny = C
        
        result.append([quarter, dime, nickel, penny])

    for i in range(case) :
        print(' '.join(map(str, result[i])))

__init__()