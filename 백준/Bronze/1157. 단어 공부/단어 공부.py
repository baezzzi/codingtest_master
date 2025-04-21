from collections import Counter

def __init__() :
    words = input().lower()
    count = Counter(words)

    common = count.most_common(2)

    if (len(common) > 1 and common[0][1] == common[1][1]) :
        print('?')
    else :
        print(common[0][0].upper())
    
__init__()