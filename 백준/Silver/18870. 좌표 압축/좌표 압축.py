import sys

def main() :
    N = int(input())

    x = list(map(int, sys.stdin.readline().split()))
    sort_x = sorted(set(x))
    
    dict_x = {val: idx for idx, val in enumerate(sort_x)}

    for n in x :
        sys.stdout.write(str(dict_x[n]) + ' ')
main()