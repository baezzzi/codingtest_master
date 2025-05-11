## 10101번 삼각형 외우기

def triangle(a, b, c) :
    if a == 60 and b == 60 and c == 60 :
        return 'Equilateral'
    elif a == b or a == c or b == c :
        return 'Isosceles'
    else :
        return 'Scalene'
    
def main() :
    a = int(input())
    b = int(input())
    c = int(input())

    if a + b + c == 180 :
        print(triangle(a, b, c))
    else :
        print('Error')

main()