def group_word(word) :
    seen = set()
    prev_char = ''

    for ch in word :
        if ch != prev_char :
            if ch in seen :
                return False
            seen.add(ch)
        prev_char = ch
    return True

def __init__() :
    n = int(input())
    result = 0

    for _ in range(n):
        word = input()
        if group_word(word) :
            result += 1

    print(result)

__init__()