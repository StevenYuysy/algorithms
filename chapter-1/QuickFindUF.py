'''
quick-find algorithm
'''

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
