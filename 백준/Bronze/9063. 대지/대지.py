## 9063번 대지

def main() :
    N = int(input())
    x, y = [], []

    for _ in range(N) :
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    resultX = max(x) - min(x)
    resultY = max(y) - min(y)

    if N == 1 :
        print(0)
    else :
        print(resultX * resultY)
    
main()