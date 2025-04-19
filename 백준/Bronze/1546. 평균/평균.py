def __init__() :
    obj = int(input())

    score = input().split()
    for i in range(obj) :
        score[i] = int(score[i])

    maxScore = max(score)

    newScore = 0

    for i in range(obj) :
        newScore += int(score[i]) / maxScore * 100

    print(newScore / obj)

__init__()
        