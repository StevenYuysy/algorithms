#! usr/bin/python
# -*- coding: utf-8 -*-

class _ListNode(object):
    """Create Listnode
    """

    def __init__(self, key):
        self.key = key
        self.next = None

class SeparateChainingHashST(object):

    def __init__(self, N):
        self._table = [None] * N
        self._N = 0 # Zero node in hash map

    def __len__(self):
        return self._N

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def get(key):
        j = self._hash(key)
        node = self._table[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            # raise KeyError, 'KeyError' + repr(key)
            return None
        return node

    def put(key):
        try:
            self[key]
        except KeyError:
            j = self._hash(key)
            node = self._table[j]
            self._table[j] = _ListNode(key)
            self._table[j].next = node
            self._n += 1
