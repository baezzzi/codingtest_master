def findNum(word) :
    first = 2
    if (word in ['A', 'B', 'C']) :
        return first + 1
    elif (word in ['D', 'E', 'F']) :
        return first + 2
    elif (word in ['G', 'H', 'I']) :
        return first + 3
    elif (word in ['J', 'K', 'L']) :
        return first + 4
    elif (word in ['M', 'N', 'O']) :
        return first + 5
    elif (word in ['P', 'Q', 'R', 'S']) :
        return first + 6
    elif (word in ['T', 'U', 'V']) :
        return first + 7
    elif (word in ['W', 'X', 'Y', 'Z']) :
        return first + 8
    else :
        print('먼가 잘못된 게 입력됨')
        return 0

def __init__() :
    words = input()
    time = 0

    for i in range(len(words)) :
        time += findNum(words[i])
    
    print(time)

__init__()