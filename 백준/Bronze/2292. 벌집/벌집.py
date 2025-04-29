def __init__() :
    num = int(input())
    distance = 1
    end_count = 1

    while num > end_count : 
        end_count += 6 * distance
        distance += 1
    
    print(distance)

__init__()