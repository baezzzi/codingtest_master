def __init__() :
    num = int(input())
    paper = [[0] * 100 for _ in range(100)]

    for i in range(num) :
        m, n = map(int, input().split())

        for i in range(n - 1, n + 9) :
            for j in range(m - 1, m + 9) :
                paper[i][j] = 1
    
    result = 0
    for i in range(100) :
        for j in range(100) :
            if paper[i][j] == 1 :
                result += 1

    print(result)

__init__()