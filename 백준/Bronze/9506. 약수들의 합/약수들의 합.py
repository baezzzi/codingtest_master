## 9506번 약수들의 합

def main() :
    result = []

    while True :
        num = 1
        divisor = []
        total = 0
        totalstr = ''

        n = int(input())
        if n == -1 :
            break

        while num < n :
            if n % num == 0 :
                divisor.append(num)
            num += 1
        
        for d in divisor :
            total += d

        if total == n :
            totalstr += ' + '.join(str(d) for d in divisor)
            result.append(f'{num} = ' + totalstr)
        else :
            result.append(f'{n} is NOT perfect.')

    for r in result :
        print(r)
main()