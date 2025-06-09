## 10773번 제로
import sys
input = sys.stdin.readline

def main() :
    result = []

    K = int(input())

    for _ in range(K) :
        num = int(input())

        if num > 0 :
            result.append(num)
        else :
            result.pop()
    
    print(sum(result))

main()