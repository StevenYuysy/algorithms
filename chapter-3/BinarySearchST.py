#! usr/bin/python
# -*- coding: utf-8 -*-

class BinarySearchST(object):

    def __init__(self):
        self.__Keys = []
        self.__Vals = []

    def get(self, key):
        N = len(self.__Keys)
        i = self.rank(key)
        if len(self.__Keys) == 0: return None
        if i < N and self.__Keys[i] == key:
            return self.__Vals[i]
        else:
            return None

    def put(self, key, val):
        N = len(self.__Keys)
        i = self.rank(key)
        # If hit, update the value
        if i < N and self.__Keys[i] == key:
            self.__Vals[i] = val
            return
        # Simlar to insertion sort, put the bigger items to the right and insert
        # to the right position if hit faild.
        else:
            j = N
            self.__Keys.append(key)
            self.__Vals.append(val)
            while i < j:
                self.__Keys[j] = self.__Keys[j-1]
                self.__Vals[j] = self.__Vals[j-1]
                j -= 1
            self.__Keys[i] = key
            self.__Vals[i] = val

    def rank(self, key):
        """BinarySearch.

        Args:
            key: Search the key in the array.

        Returns:
            mid: The position that already exist the key.
            lo: The position that key can insert.
        """
        lo = 0
        hi = len(self.__Keys) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.__Keys[mid] > key:
                hi = mid - 1
            elif self.__Keys[mid] < key:
                lo = mid + 1
            else:
                return mid
        return lo

    def contains(self, key):
        N = len(self.__Keys)
        i = self.rank(key)
        if len(self.__Keys) == 0: return False
        if i < N and self.__Keys[i] == key:
            return True
        else:
            return False

    def keys(self):
        return self.__Keys


if __name__ == "__main__":

    st = BinarySearchST()
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
