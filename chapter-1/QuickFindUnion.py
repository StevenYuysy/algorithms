'''
quick-union algorithm
'''

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

with open('../test-data/mediumUF.txt', 'r') as f:
    # read the site counts
    N = int(f.readline())
    uf = UF(N)

    for line in f.readlines():
        readIn = line.strip().split(' ')
        p = int(readIn[0])
        q = int(readIn[1])
        if (uf.connected(p, q)):
            continue
        uf.union(p, q)
        print '%d %d' %(p, q)

    print '%d components' % uf.count
