import math

def prime(n) :
    if n < 2 :
        return False
    elif n == 2 :
        return True
    elif n % 2 == 0 :
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2) :
        if n % i == 0 :
            return False
        
    return True
        
def main() :
    case = int(input())

    result = []

    for _ in range(case) :
        n = int(input())

        while True :
            if prime(n) :
                result.append(n)
                break
            n += 1

    for r in result :
        print(r)

main()