## 1181번 단어 정렬
def main() :
    N = int(input()) 
    
    wordset = set()

    for _ in range(N) :
        word = input()

        wordset.add(word)

    words = list(wordset)
    
    words.sort(key=lambda x: (len(x), x))

    for w in words :
        print(w)

main()