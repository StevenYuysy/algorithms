#! usr/bin/python
# -*- coding: utf-8 -*-

class _ListNode(object):
    """Create Listnode
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class SeparateChainingHashST(object):

    def __init__(self, N):
        self._table = [None] * N
        self._N = 0 # Zero node in hash map

    def __len__(self):
        return self._N

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def get(self, key):
        j = self._hash(key)
        node = self._table[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.val

    def put(self, key, val):
        j = self._hash(key)
        node = self._table[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            node = self._table[j]
            self._table[j] = _ListNode(key, val)
            self._table[j].next = node
            self._N += 1
        else:
            node.val = val

    def contains(self, key):
        j = self._hash(key)
        node = self._table[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return False
        return True

    def keys(self):
        arr = []
        for i in self._table:
            if i is not None:
                arr.append(i.key)
                while i.next is not None:
                    i = i.next
                    arr.append(i.key)
        return arr

if __name__ == "__main__":

    st = SeparateChainingHashST(997)
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
