## 3009번 네 번째 점
from collections import Counter

def main() :
    x = []
    y = []
    
    for _ in range(3) :
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    countX = Counter(x)
    countY = Counter(y)

    resultX = [k for k, v in countX.items() if v == 1][0]
    resultY = [k for k, v in countY.items() if v == 1][0]

    print(resultX, resultY)
main()