from string import ascii_uppercase

def __init__() :
    alphabet = list(ascii_uppercase)
    zin = [i + 10 for i in range(36)]
    formation = dict(zip(alphabet, zin))

    N, B = input().split()
    B = int(B)

    result = 0

    for i in range(len(N)) : 
        ch = N[-(i + 1)]
        if ch.isdigit() :
            val = int(ch)
        else :
            val = formation[N[-(i + 1)]]
        
        result += val * (B ** i)
        
    print(result)

__init__()