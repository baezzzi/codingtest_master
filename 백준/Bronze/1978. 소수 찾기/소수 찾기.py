## 1978번 소수 찾기

def main() :
    case = int(input())

    num = input().split()

    count = 0

    for i in range(case) :
        divisor = []
        n = 1
        num[i] = int(num[i])
        while n <= num[i] :
            if num[i] % n == 0 :
                divisor.append(n)
            n += 1
        
        if len(divisor) == 2 :
            count += 1
        
    print(count)

main()
