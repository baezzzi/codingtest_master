import sys

def main() :
    N = int(input())
    sanggeun = set(map(int, input().split()))

    M = int(input())
    cards = list(map(int, input().split()))

    count = []

    for c in cards :
        if c in sanggeun :
            count.append('1')
        else :
            count.append('0')
    print(' '.join(count))

main()