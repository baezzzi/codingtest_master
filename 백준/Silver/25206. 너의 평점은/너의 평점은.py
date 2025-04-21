score = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5][::-1]
grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

credit = dict(zip(grade, score))

def __init__() :
    n = 0
    total = 0
    totalnum = 0
    while (n < 20) :
        obj, num, mark = input().split()
        num = float(num)
        if (mark == 'P') :
            n += 1
            continue
        else :
            totalnum += num
            total += num * credit[mark]
            n += 1
    print(total / totalnum)
    

__init__()