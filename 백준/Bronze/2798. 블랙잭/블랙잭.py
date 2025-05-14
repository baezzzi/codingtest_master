## 2789번 블랙잭

def main() :
    N, M = map(int, input().split())

    card = list(map(int, input().split()))
    blackjack = 0

    for i in range(N) :
        for j in range(i + 1, N) :
            for k in range(j + 1, N) :
                total = 0   
                total += card[i] + card[j] + card[k]
                if total <= M and total > blackjack :
                    blackjack = total

    print(blackjack)
main()