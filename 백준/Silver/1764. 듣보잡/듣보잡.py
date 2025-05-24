def main() :
    N, M = map(int, input().split())
    noListen = set()
    both = []

    for _ in range(N) :
        noListen.add(input())
    
    for _ in range(M) :
        name = input()

        if name in noListen :
            both.append(name)
    
    both.sort()
    print(len(both))
    
    for b in both :
        print(b)

main()