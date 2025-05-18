def main() :
    N = int(input())
    count = []

    for x in range(N // 5 + 1) :
        for y in range(N // 3 + 1) :
            if 5 * x + 3 * y == N :
                count.append(x + y)
    
    if len(count) == 0 :
        print(-1)
    else :
        print(min(count))

main()