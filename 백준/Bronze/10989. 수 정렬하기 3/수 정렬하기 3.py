import sys

def main() :
    N = int(input())

    count = [0] * 10001

    for _ in range(N) :
        count[int(sys.stdin.readline())] += 1
    
    for i in range(len(count)) :
        for _ in range(count[i]) :
            sys.stdout.write(str(i) + '\n')

main()