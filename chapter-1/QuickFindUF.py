#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Quick-find.
It maintains the invariant that p and q are connected if and only if id[p] is
equal to id[q]. In other words, all sites in a component must have the same
value in id[].
快速查找算法。
一种方法是保证当且仅当 id[p] 等于 id[q] 时 p 和 q 是连通的。换句话说，在同一个连通中的所有
触点在 id[] 的值必须全部相同。
'''
from time import time

class UF(object):

    def __init__(self, N):
        self.count = N
        self.id = [n for n in range(N)]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return

        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
        self.count -= 1

with open('../test-data/largeUF.txt', 'r') as f:
    # read the site counts
    N = int(f.readline())
    uf = UF(N)
    start = time()
    for line in f.readlines():
        readIn = line.strip().split(' ')
        p = int(readIn[0])
        q = int(readIn[1])
        if (uf.connected(p, q)):
            continue
        uf.union(p, q)
        print '%d %d' %(p, q)
    end = time()
    print '%d components \n %s' % (uf.count, end-start)
