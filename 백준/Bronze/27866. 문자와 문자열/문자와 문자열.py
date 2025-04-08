def findWord(word, num):
    if (num > len(word)) :
        print("글자 수보다 큰 수를 입력하였습니다.")
    else :
        print(word[num-1])

def __init__() :
    word = input()
    num = int(input())
    
    findWord(word, num)

__init__()