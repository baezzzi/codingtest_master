def main() :
    N, M = map(int, input().split())

    S = set()
    count = 0

    for _ in range(N) :
        S.add(input())

    for _ in range(M) :
        string = input()
        if string in S :
            count += 1
    
    print(count)

main()