import sys
def main() :
    N = input()

    count = [0] * 10 
    result = []

    for i in range(len(N)) :
        count[int(N[i])] += 1
    
    for i in range(10) :
        for _ in range(count[i]) :
            result.append(i)
    
    result = result[::-1]
    
    for i in range(len(result)) :
        sys.stdout.write(str(result[i]))
main()