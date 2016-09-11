if __name__ == "__main__":

    st = {}
    minlen = int(input('> min length of the word: '))

    print('> searching tale.txt...')
    with open('../test-data/tale.txt') as f:
        for dataIn in f.readlines():
            for word in dataIn.strip().split():
                if len(word) < minlen: continue
                if word not in st:
                    st[word] = 1
                else:
                    st[word] = st[word] + 1

    maxWord = ''
    maxVal = 0
    for word, val in st.items():
        if val > maxVal:
            maxVal = val
            maxWord = word
    print('> most frequent word: %s %s' % (maxWord, maxVal))
