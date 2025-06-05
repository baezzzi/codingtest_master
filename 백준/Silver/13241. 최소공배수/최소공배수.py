## 13241번 최소공배수

def gcd(a, b) :
    while b :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return a * b // gcd(a, b)

def main() :
    A, B = map(int, input().split())
    print(lcm(A, B))

main()