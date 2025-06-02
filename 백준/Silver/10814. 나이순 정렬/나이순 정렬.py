## 10814번 나이순 정렬
import sys

def main() :
    N = int(input())

    signup = []

    for i in range(N) :
        age, name = sys.stdin.readline().split()
        signup.append((age, name, i))
        
    people = sorted(signup, key=lambda x: (int(x[0]), x[2]))

    for p in people :
        sys.stdout.write(p[0] + ' ' + p[1] + '\n')

main()