def countNum(m, n, gap):
    return set(range(m, n + 1, gap))

def main():
    M, N = map(int, input().split())

    prime = set()
    if N >= 2: prime.add(2)
    if N >= 3: prime.add(3)

    prime |= set(range(5, N + 1, 6)) | set(range(7, N + 1, 6))

    limit = int(N ** 0.5) + 1
    for i in range(5, limit, 6):
        if i in prime:
            prime -= set(range(i * i, N + 1, i))
        j = i + 2
        if j in prime:
            prime -= set(range(j * j, N + 1, j))

    for p in sorted(prime):
        if p >= M:
            print(p)

main()
