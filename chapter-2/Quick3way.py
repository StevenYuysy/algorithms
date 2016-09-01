#! usr/bin/pyhton
# -*- coding: utf-8 -*-

"""
Quicksort with 3-way.

It perform much better than standard quick sort while sorting an array with lots
of repeating elements.

三向切分的快速排序。

对于存在大量重复元素的数组，这种方法比标准的快速排序的效率高得多。
"""

def quick3way(array):

    def sort(lo, hi):
        if hi <= lo: return
        lt = lo
        i = lo + 1
        gt = hi
        v = array[lo]
        while i <= gt:
            if array[i] < v:
                array[lt], array[i] = array[i], array[lt]
                lt += 1
                i += 1
            elif array[i] > v:
                array[i], array[gt] = array[gt], array[i]
                gt -= 1
            else:
                i += 1

        sort(lo, lt - 1)
        sort(gt + 1, hi)

    sort(0, len(array)-  1)
    return array

if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    data = getRandomNumbers(0, 1000, 15)
    print('Quick-three-way Sort')
    print('> input: %s' % data)
    print('> output: %s' % quick3way(data))
