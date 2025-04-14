def iterWord(num, words) :
    result = ''
    for i in range(len(words)) :
        result += words[i] * num

    print(result)

def __init__() :
    testcase = int(input())

    for i in range(testcase) :
        num_str, words = input().split()
        num = int(num_str)
        iterWord(num, words)

__init__()
