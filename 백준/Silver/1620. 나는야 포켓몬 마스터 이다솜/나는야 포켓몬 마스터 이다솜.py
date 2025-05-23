## dict
import sys

def main() :
    pokemon_num = {}
    pokemon_name = {}

    result = []

    N, M = map(int, sys.stdin.readline().split())
    
    for i in range(N) :
        name = input()
        pokemon_name[name] = i + 1
        pokemon_num[i + 1] = name
    
    for _ in range(M) :
        quiz = input()
        
        if quiz.isdigit() :
            result.append(pokemon_num[int(quiz)])
        else :
            result.append(pokemon_name[quiz])

    for r in result :
        sys.stdout.write(str(r) + '\n')
    
main()