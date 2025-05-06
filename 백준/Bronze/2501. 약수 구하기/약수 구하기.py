## 2501번 약수 구하기

def main() :
    N, K = map(int, input().split())

    divisor = []
    num = 1
    while num <= N :
        if N % num == 0 :
            divisor.append(num)
        num += 1
    
    if K > len(divisor) :
        print(0)
    else :
        print(divisor[K - 1])
main()