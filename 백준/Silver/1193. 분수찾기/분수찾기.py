## 1193번 분수 찾기

def __init__() :
    line = 1
    num = int(input())

    while line < num :
        num -= line
        line += 1

    if line % 2 == 0 :
        up = num
        down = line - num +  1
    else : 
        up = line - num + 1
        down = num
    print(f'{up}/{down}')

__init__()
    