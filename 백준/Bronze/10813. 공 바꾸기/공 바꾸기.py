def __init__() :
    N, M = input().split()
    N, M = int(N), int(M)
    basket = [i + 1 for i in range(N)]
    result = ''

    for m in range(M) :
        i, j = input().split()
        i, j = int(i), int(j)
        
        hi = basket[i - 1]
        basket[i - 1] = basket[j - 1]
        basket[j - 1] = hi
    
    for m in range(N) :
        result += (str(basket[m]) + ' ')
    
    print(result)

__init__()