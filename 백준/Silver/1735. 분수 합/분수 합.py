
## 1735번 분수 합
def gcd(a, b) :
    while b :
        a, b = b, a % b
    return a

def fraction(a, b, c, d) :
    bj = a * d + b * c
    bm = b * d
    return bj // gcd(bj, bm), bm // gcd(bj, bm)

def main() :
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    
    bj, bm = fraction(A, B, C, D)

    print(bj, bm)

main()