def __init__() :
    N = int(input())
    space = ' '
    star = '*'

    for i in range(N) :
        print(f'{space * (N - i - 1)}{star * (2 * i + 1)}')
    for i in range(N - 1) :
        print(f'{space * (i + 1)}{star * (2 * N - (2 * i + 3))}')
        

__init__()