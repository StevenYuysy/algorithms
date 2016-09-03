#! usr/bin/python
# -*- coding: utf-8 -*-

from SequentialSearchST import SequentialSearchST


st = SequentialSearchST()
minlen = int(input('> min length of the word: '))

print('> searching tale.txt...')
with open('../test-data/tale.txt') as f:
    for dataIn in f.readlines():
        for word in dataIn.strip().split():
            if len(word) < minlen: continue
            if not st.contains(word):
                st.put(word, 1)
            else:
                st.put(word, st.get(word)+1)


max = ''
st.put(max, 0)
for word in st.keys():
    if st.get(word) > st.get(max):
        max = word
print('> most frequent word: %s %s' % (max, st.get(max)))
