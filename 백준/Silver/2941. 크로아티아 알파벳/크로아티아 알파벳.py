## 2941번 크로아티아 알파벳

def __init__() :
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    word = input()
    
    for i in croatia :
        word = word.replace(i, '*')
    
    print(len(word))

__init__()