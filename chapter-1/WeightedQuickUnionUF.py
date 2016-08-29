#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Weighted quick-union.
Rather than arbitrarily connecting the second tree to thefirst for union() in
the quick-union algorithm, we keep track of the size ofeach tree and always
connect the smaller tree to the larger.
加权快速连通。
与其在 union() 中随意将一棵树连接到另一棵树，我们现在会记录每一棵树的大小并总是
将较小的树连接到较大的树上。
"""

from time import time

class UF(object):

    def __init__(self, N):
        self.count = N
        self.id = [n for n in range(N)]
        self.size = [1 for n in range(N)]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        # find the root of the point
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return

    # add weighted to ensure that the smaller one always add to the bigger one
        if self.size[pRoot] > self.size[qRoot]:
            self.id[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]
        else:
            self.id[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]

        self.count -= 1

if __name__ == "__main__":

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
        print '%d components \ntotal time: %s' % (uf.count, end-start)
