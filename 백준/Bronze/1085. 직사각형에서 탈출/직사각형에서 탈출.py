## 1085번 직사각형에서 탈출

def main() :
    x, y, w, h = map(int, input().split())
    
    diffX = w - x
    diffY = h - y

    print(min(diffX, diffY, x, y))

main()