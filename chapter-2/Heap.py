#! usr/bin/python
# -*- coding: utf-8 -*-

"""
Heap sort

堆排序
"""

def Heap(array):

    def sink(array, k, N):
        while 2 * k <= N:
            j = 2 * k
            if j < N and array[j] < array[j+1]: j += 1
            if not array[k] < array[j]: break
            array[k], array[j] = array[j], array[k]
            k = j

    # Build heap
    N = len(array) - 1
    k = N // 2
    while k >= 1:
        # print('sink(array, %d, %d)' % (k, N))
        sink(array, k, N)
        k -= 1
    # Sink sort
    while N > 1:
        # print('exch(array, 1, %d)' % N)
        array[1], array[N] = array[N], array[1]
        N -= 1
        # print('sink(array, 1, %d)' % N)
        sink(array, 1, N)

    return array

if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    data = getRandomNumbers(0, 1000, 15)
    data[0] = None
    print('Heap Sort')
    print('> input %s' % data)
    print('> output %s ' % Heap(data))
