def main() :
    N = int(input())

    start = max(1, N - len(str(N)) * 9)
    for i in range(start, N) :
        a = i + sum(map(int, str(i)))
        
        if a == N :
            print(i)
            return
    print(0)
main()