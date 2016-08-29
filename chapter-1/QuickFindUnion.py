#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Quick-union.
It is based on the same data structure—the site-indexed id[] array—but it uses a
different interpretation of the values that leads to more complicated structures.
Specifically, the id[] entry for each site will be the name of another site in
the same component (possibly itself). To implement find() we start at the given
site, follow its link to another site, follow that sites link to yet another
site, and so forth, following links until reaching a root, a site that has a
link to itself. Two sites are in the same component if and only if this process
leads them to the same root. To validate this process, we need union() to
maintain this invariant, which is easily arranged: we follow links to find the
roots associated with each of the given sites, then rename one of the components
by linking one of these roots to the other.
快速连通算法。
它基于同样的数据结构-以触点作为索引的 id[] 数组，但我们赋予这些值的意义不同，我们需要用它们来
定义更加复杂的结构。确切的说，每个触点所对应的 id[] 元素都是同一个分量中的另一个触点的名称（也
有可能是它自己）我们将这种方法称为链接。在实现 find() 方法时，我们从给定的触点开始，由它的链接
得到另一个触点，再由这个触点的链接到达第三个触点，如此继续跟随着链接直到到达一个跟触点。
"""

from time import time

class UF(object):

    def __init__(self, N):
        self.count = N
        self.id = [n for n in range(N)]

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

        self.id[pRoot] = qRoot
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
