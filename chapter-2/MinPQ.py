class MinPQ(object):
    """The MinPQ class represents a priority queue.

    This implementation uses a binary heap.

    Attributes:
        __queue: A priority queue.
    """

    def __init__(self):
        """Init a priority queue, we do not use index 0."""
        self.__queue = [None]

    def __greater(self, i, j):
        """Compare that wether i is greater than j.

        Returns:
            A boolean.
        """
        return self.__queue[i] > self.__queue[j]

    def __exch(self, i, j):
        """Change the index i and j in priority queue."""
        self.__queue[i], self.__queue[j] = self.__queue[j], self.__queue[i]

    def __swim(self, k):
        """Helper functions to restore the heap invariant."""
        while k > 1 and self.__greater(k//2, k):
            self.__exch(k//2, k)
            k = k // 2

    def __sink(self, k):
        """Helper functions to restore the heap invariant."""
        N = self.size()
        while 2 * k <= N:
            j = 2 * k
            if j < N and self.__greater(j, j+1): j += 1
            if not self.__greater(k, j): break
            self.__exch(k, j)
            k = j

    def isEmpty(self):
        """Check is length is empty.

        Returns:
            A boolean.
        """
        return len(self.__queue) == 1

    def size(self):
        """The length of the priority queue, ignore index 0.

        Returns:
            A number.
        """
        return len(self.__queue) - 1


    def insert(self, v):
        """Insert a value into priority queue."""
        self.__queue.append(v)
        N = self.size()
        self.__swim(N)

    def delMin(self):
        """Remove the minimum number of the priority queue.

        Returns:
            A number: the minimum number.
        """
        N = self.size()
        min = self.__queue[1]
        self.__exch(1, N)
        self.__queue.pop()
        self.__sink(1)
        return min


if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    data = getRandomNumbers(0, 100, 10)
    M = 5
    print('test-data: %s' % data)
    print('test-size: %d' % M)
    pq = MinPQ()
    result = []
    for i in range(len(data)-1):
        pq.insert(data[i])
        if pq.size() > M: pq.delMin()

    while not pq.isEmpty(): result.append(pq.delMin())
    print('result %s' % result)
