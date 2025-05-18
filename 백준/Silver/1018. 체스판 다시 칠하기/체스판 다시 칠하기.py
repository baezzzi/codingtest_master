def main() :
    N, M = map(int, input().split()) 

    chess = [input() for _ in range(N)]

    result = 64

    for i in range(N - 7) :
        for j in range(M - 7) :
            B, W = 0, 0

            for x in range(8) :
                for y in range(8) :
                    current = chess[i + x][j + y] ## 현채 위치한 체스판 위치

                    if (x + y) % 2 == 0 :
                        if  current != 'W' :
                            W += 1
                        if current != 'B' :
                            B += 1
                    else :
                        if current != 'W' :
                            ## 홀수일 때는 해당하지 않은 색이 하나 더 많아야됨
                            B += 1
                        if current != 'B' :
                            W += 1
            result = min(result, B, W)
    print(result)

main()