## 7785번 회사에 있는 사람
import sys

def main() :
    n = int(input())

    people = set()

    for _ in range(n) :
        name, state = sys.stdin.readline().split()
        
        if state == 'enter' :
            people.add(name)
        elif state == 'leave' and name in people :
            people.remove(name)

    people = list(people)
    people.sort(reverse=True)
    for p in people :
        sys.stdout.write(p + "\n")

main()