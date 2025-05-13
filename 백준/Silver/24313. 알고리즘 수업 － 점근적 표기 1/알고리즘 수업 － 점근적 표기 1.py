## 24313번 알고리즘 어쩌구

def f(n, a1, a0) :
    return a1 * n + a0

def g(n) :
    return n

def main() : 
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())

    for i in range(n0, 101) :
        if f(i, a1, a0) > c * g(i) :   
            print(0)
            return
    print(1)
main()