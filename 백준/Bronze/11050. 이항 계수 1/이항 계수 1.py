## 11050번 이항계수
import sys
input = sys.stdin.readline

def nCk(n, k) :
    bj = 1
    bm = 1
    for i in range(n - k + 1 , n + 1) :
        bj *= i
    
    for i in range(1, k + 1) :
        bm *= i
    
    return int(bj / bm)

def main() :
    N, K = map(int, input().split())
    print(nCk(N, K))

main()