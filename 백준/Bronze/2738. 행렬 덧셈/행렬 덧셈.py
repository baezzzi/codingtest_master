## 2738번 행렬 덧셈

def __init__() :
    N, M = map(int, input().split())
    A, B = [], []
    result = []

    for i in range(N) :
        A.append(list(map(int, input().split())))

    for i in range(N) :
        B.append(list(map(int, input().split())))

    for i in range(N) :
        for j in range(M) :
            print(A[i][j] + B[i][j], end = ' ')
        print()

__init__()