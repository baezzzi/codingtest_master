## 2581번 소수

def main() :
    M = int(input())
    N = int(input())

    total = 0
    result = []

    for i in range(M, N + 1) :
        factor = []
        num = 1
        # 약수 찾기
        while num <= i :
            if i % num == 0 :
                factor.append(num)
            num += 1
        # 소수면 result에 추가
        if len(factor) == 2 :
            result.append(i) 
            total += i
            
    if len(result) >= 1 :
        print(total)
        print(min(result))
    else :
        print(-1)

main()