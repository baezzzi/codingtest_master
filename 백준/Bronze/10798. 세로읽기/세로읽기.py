def __init__() :
    numlen = []
    words = []

    result = ''
    for _ in range(5) : 
        words += input().split()

    for i in range(5) :
        numlen.append(len(words[i]))

    for i in range(max(numlen)) :
        for j in range(5):
            if(len(words[j]) - 1 >= i) : 
                result += ''.join(map(str, words[j][i]))

            
    print(result)
__init__()
