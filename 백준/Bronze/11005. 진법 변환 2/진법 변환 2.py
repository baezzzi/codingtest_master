from string import ascii_uppercase

def __init__() :
    formation = [str(i) for i in range(10)] + list(ascii_uppercase)

    result = ''
    
    N, B = map(int, input().split())

    while N > 0 :
        N, reminder = divmod(N, B) 
        result += formation[reminder]
    
    print(result[::-1])

__init__()