#! usr/bin/python
# -*- coding: utf-8 -*-

_RED = True
_BLACK = False

class _Node(object):

    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.color = color
        self.left = None
        self.right = None

class RedBlackBST(object):

    def __init__(self):
        self.__root = None

    def __isRed(self, x):
        if x == None: return False
        return x.color == _RED

    def __rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = _RED
        return x

    def __rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = _RED
        return x

    def __flipColors(self, h):
        h.color = _RED
        h.left.color = _BLACK
        h.right.color = _BLACK

    def put(self, key, val):
        self.__root = self.__put(self.__root, key, val)
        self.__root.color = _BLACK

    def __put(self, h, key, val):
        if h == None: return _Node(key, val, _RED)
        if key < h.key:
            h.left = self.__put(h.left, key, val)
        elif key > h.key:
            h.right = self.__put(h.right, key, val)
        else:
            h.val = val

        if self.__isRed(h.right) and self.__isRed(h.left):
            h =self. __rotateLeft(h)
        if self.__isRed(h.left) and self.__isRed(h.left.left):
            h = self.__rotateRight(h)
        if self.__isRed(h.left) and self.__isRed(h.right):
            self.__flipColors(h)

        return h

    def get(self, key):
        return self.__get(self.__root, key)

    def __get(self, x, key):
        if x == None: return None
        if key < x.key:
            return self.__get(x.left, key)
        elif key > x.key:
            return self.__get(x.right, key)
        else:
            return x.val

    def contains(self, key):
        if self.get(key):
            return True
        else:
            False

    def keys(self):
        arr = []

        def preorder(node):
            if node is not None:
                arr.append(node.key)
                preorder(node.left)
                preorder(node.right)

        preorder(self.__root)
        return arr

if __name__ == "__main__":

    st = RedBlackBST()
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
