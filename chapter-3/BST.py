#! ust/bin/python
# -*- coding: utf-8 -*-

class _Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class BST(object):

    def __init__(self):
        self.__root = None

    def get(self, key):
        return self.__get(self.__root, key)

    def __get(self, x, key):
        """Find the key's value and return it in the tree based on x as root
        node.

        Args:
            x: root node.
            key: the corresponding key.

        Returns:
            x.val: node's value.
        """
        if x == None: return None
        if key < x.key:
            return self.__get(x.left, key)
        elif key > x.key:
            return self.__get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        self.__root = self.__put(self.__root, key, val)

    def __put(self, x, key, val):
        """Find the key and update the value in the tree based on x as root
        node, else insert the key and value to the tree.

        Args:
            x: root node.
            key: the corresponding key.
            value: the corresponding value.

        Returns:
            x: root node.

        """
        if x == None: return _Node(key, val)
        if key < x.key:
            x.left = self.__put(x.left, key, val)
        elif key > x.key:
            x.right = self.__put(x.right, key, val)
        else:
            x.val = val
        return x

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

    st = BST()
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
