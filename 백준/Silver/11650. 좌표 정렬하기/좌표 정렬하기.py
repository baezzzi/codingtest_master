## 11650번 좌표 정렬하기
def main() :
    N = int(input())

    dimnesion2 = []

    for _ in range(N) :
        dimnesion2.append(list(map(int, input().split())))

    dimnesion2.sort()

    for i in range(N) :
        print(dimnesion2[i][0], dimnesion2[i][1])

main()