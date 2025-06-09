## 28278번 스택 2
import sys
input = sys.stdin.readline
stack = []
result = []

def fun1(x) :
    stack.append(x)

def fun2() :
    if len(stack) > 0 :
        result.append(stack.pop())
    else :
        result.append(-1)
    
def fun3() :
    result.append(len(stack))

def fun4() :
    if len(stack) > 0 :
        result.append(0)
    else :
        result.append(1)

def fun5() :
    if len(stack) > 0 :
        result.append(stack[-1])
    else :
        result.append(-1)

def main() :
    N = int(input())

    for _ in range(N) :
        cmd = list(map(int, input().split()))

        if cmd[0] == 1 :
            fun1(cmd[-1])
        elif cmd[0] == 2 :
            fun2()
        elif cmd[0] == 3 :
            fun3()
        elif cmd[0] == 4 :
            fun4()
        elif cmd[0] == 5 :
            fun5()
            
    for r in result :
        print(r)

main()