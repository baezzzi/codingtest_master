result = []

def firstNend(word, wordlen) : 
    feword = word[0]+word[wordlen-1]
    result.append(feword)

def __init__() :
    num = int(input()) # 테스트케이스 개수 입력
    if (num < 1 or num > 10) :
        return 0

    for i in range(num) :
        word = input()
        wordlen = len(word)

        if (len(word) > 1000) :
            return 0
        
        firstNend(word, wordlen)
    
    for i in range(num) :
        print(result[i])

__init__()
    