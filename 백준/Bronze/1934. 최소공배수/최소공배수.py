
def gcd(a, b) :
    while b :
        a, b = b, a % b
    return a
    
def lcm(a, b) :
    return a * b // gcd(a, b)

def main() :
    case = int(input())
    result = []

    for _ in range(case) :
        A, B = map(int, input().split())
        
        result.append(lcm(A, B))
    
    for r in result :
        print(r)

main()        