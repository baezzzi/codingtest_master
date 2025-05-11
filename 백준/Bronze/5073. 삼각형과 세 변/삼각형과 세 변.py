## 5073번 삼각형과 세 변

def triangle(a, b, c) :
    if a == b == c :
        return 'Equilateral'
    elif a == b or b == c or a == c :
        return 'Isosceles'
    else :
        return 'Scalene'
    
def main() :
    result = []
    while True :
        n = list(map(int, input().split()))
        n.sort(reverse=True)
        a = n[0]
        b = n[1]
        c = n[2]

        if a == b == c == 0 :
            for r in result :
                print(r)
            break

        if a < b + c :
            result.append(triangle(a, b, c))
        else :
            result.append('Invalid')

main()