def __init__() :
    words = input()
    result = []

    for i in range(len(words)) :
        if (words[i] == words[-i -1]) :
            result.append(1)
        else :
            result.append(0)
    if (0 in result) :
        print(0)
    else :
        print(1)

__init__()