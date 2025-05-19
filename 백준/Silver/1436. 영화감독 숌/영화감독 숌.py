
def main() :
    N = int(input()) 
    nth = 0
    num = 666
    
    
    while True :
        str_num = str(num)

        if '666' in str_num :
            nth += 1
        
        if nth == N :
            break

        num += 1
    
    print(num)

main()