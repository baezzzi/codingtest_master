import math

def __init__() :
    A, B, V = map(int, input().split())

    print(math.ceil((V - B) / (A - B)))

__init__()