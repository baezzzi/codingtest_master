from string import ascii_lowercase
alphabet = list(ascii_lowercase)
result = []

def __init__() :
    s = input()

    for i in range(len(alphabet)) :
        result.append(s.find(alphabet[i]))

    for j in range(len(alphabet)) :
        print(result[j], end=' ')
    print()

__init__()