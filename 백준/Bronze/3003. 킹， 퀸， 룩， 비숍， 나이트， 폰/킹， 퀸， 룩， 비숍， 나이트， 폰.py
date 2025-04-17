chess = [1, 1, 2, 2, 2, 8]

def __init__() :
    white = input().split()

    for i in range(len(chess)) :
        print(chess[i] - int(white[i]))

__init__()