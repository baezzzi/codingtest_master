def main() :
    stick = list(map(int, input().split()))
    stick.sort(reverse=True)
    a = stick[0]
    b = stick[1]
    c = stick[2]

    while True :
        if a < b + c :
            print(a + b + c)
            break
        else :
            a -= 1
    
main()