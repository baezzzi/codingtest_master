## 5086번 배수와 약수
def Relation(a, b) :
    if b % a == 0 :
        return 'factor'
    elif a % b == 0 :
        return 'multiple'
    else : 
        return 'neither'

def main() :
    result = []
    while True :
        a, b = map(int, input().split())
        if a == 0 and b == 0 :
            break
        result.append(Relation(a, b))
    
    for i in range(len(result)) :
        print(result[i])
    
main()