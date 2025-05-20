import statistics
def avg(numbers) :
    total = 0
    for i in range(5) :
        total += numbers[i]

    return total // 5
def main() :
    numbers = []
    for _ in range(5) :
        numbers.append(int(input()))

    print(avg(numbers))
    print(statistics.median(numbers))

main()