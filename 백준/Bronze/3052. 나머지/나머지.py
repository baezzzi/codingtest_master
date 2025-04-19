from collections import Counter
def __init__() :
    numbers = []
    for i in range(10) :
        num = int(input())
        numbers.append(num % 42)
        
    result = Counter(numbers)
    print(len(result))

__init__()