class MinPQ(object):
    """The MinPQ class represents a priority queue.

    This implementation uses a binary heap.

    Attributes:
        _queue: A priority queue.
    """

    def __init__(self):
        """Init a priority queue, we do not use index 0."""
        self._queue = [None]

    def __greater(self, i, j):
        """Compare that is i greater than j.

        Returns:
            A boolean.
        """
        return self._queue[i] > self._queue[j]

    def __exch(self, i, j):
        """Change the index i and j in priority queue."""
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]

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
        return len(self._queue) == 1

    def size(self):
        """The length of the priority queue, ignore index 0.

        Returns:
            A number.
        """
        return len(self._queue) - 1


    def insert(self, v):
        """Insert a value into priority queue."""
        self._queue.append(v)
        N = self.size()
        self.__swim(N)

    def delMin(self):
        """Remove the maximum of the priority queue."""
        N = self.size()
        min = self._queue[1]
        self.__exch(1, N)
        self._queue.pop()
        self.__sink(1)
        return min


if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    input = getRandomNumbers(0, 100, 10)
    M = 5
    print('test-data: %s' % input)
    print('test-size: %d' % M)
    pq = MinPQ()
    result = []
    for i in range(len(input)-1):
        pq.insert(input[i])
        if pq.size() > M: pq.delMin()

    while not pq.isEmpty(): result.append(pq.delMin())
    print('result %s' % result)
