## 2751번 수 정렬하기2
import sys
def main() :
    N = int(input())

    numbers = []

    for _ in range(N) :
        numbers.append(int(sys.stdin.readline()))

    numbers.sort()
    
    for n in numbers :
        print(n)
    
main()