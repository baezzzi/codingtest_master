
## 19532번 수학은 비대면강의입니다.
def fun1st(a, b, c, d, e, f) :

    y = int((d * c - a * f) / (d * b - a * e))
    x = int((e * c - b * f) / (e * a - b * d))

    print(x, y)


def main() :
    a, b, c, d, e, f = map(int, input().split())
    
    if a == b == c == d == e == f :
        return
    else :
        fun1st(a, b, c, d, e, f)

main()