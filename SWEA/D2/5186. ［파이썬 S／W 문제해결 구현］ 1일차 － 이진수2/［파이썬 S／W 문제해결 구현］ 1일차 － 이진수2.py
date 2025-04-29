def __init__() :
    case = int(input())
    result = []

    for t in range(case) :
        num = float(input())
        twozin = ''

        while num > 0 and len(twozin) <= 12:
            num *= 2
            if num >= 1:
                twozin += '1'
                num -= 1
            else:
                twozin += '0'

        if len(twozin) > 12:
            result.append('overflow')
        else:
            result.append(twozin)

    for i in range(case) :
        print(f'#{i + 1} {result[i]}')

__init__()
