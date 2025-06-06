import sys
input = sys.stdin.readline
from math import gcd

def main() :
    N = int(input())

    trees = []
    gaps = []
    
    for i in range(N) :
        tree = int(input())
        trees.append(tree)
    
        if i > 0 :
            gaps.append(tree - trees[i - 1])
    
    a = gaps[0]
    for i in range(1, N - 1) :
        a = gcd(a, gaps[i])

    print((trees[N -1] - trees[0]) // a - N + 1)

main()