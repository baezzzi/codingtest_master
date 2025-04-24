def __init__() :
    gugu = []
    maxnum = -1
    maxX = 0
    maxY = 0

    for _ in range(9) :
        gugu.append(list(map(int, input().split())))
    
    for i in range(9) :
        for j in range(9) :
            if gugu[i][j] > maxnum :
                maxnum = gugu[i][j]
                maxX = i + 1
                maxY = j + 1

    print(maxnum)
    print(maxX, maxY, end = ' ')

__init__()