def main() :
    S = input()

    strset = set()

    for i in range(len(S)) :
        strset.add(S[i])
        for j in range(i + 1, len(S) + 1) :
            strset.add(S[i:j])
    strset.add(S)

    print(len(strset))

main()
        