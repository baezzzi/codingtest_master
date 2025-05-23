from collections import Counter

def main() :
    N = int(input())

    card = list(map(int, input().split()))
    cardset = set(card)

    sgCard = dict(Counter(card))

    result = []

    M = int(input())
    
    numbers = list(map(int, input().split()))

    for i in range(M) :
        if numbers[i] in cardset :
            result.append(sgCard[numbers[i]])
        else :
            result.append(0)
    
    print(' '.join(map(str, result)))
        

main()