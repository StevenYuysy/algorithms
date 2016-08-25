#! usr/bin/python
# -*- coding: utf-8 -*-

'''
Shellsort

Shellsort is a simple extension of insertion sort that gains speed by allowing
exchanges of entries that are far apart, to produce partially sorted arrays
that can be efficiently sorted, eventually by insertion sort. The idea is to
rearrange the array to give it the property that taking every hth entry
(starting anywhere) yields a sorted sequence.

Worst case performance	O(nlog2^2 n)
Best case performance O(n)
Average case performance depends on gap sequence

希尔是插入排序的简单延伸，相距甚远的元素通过不同的步长进行交换，产生部分排序的数组可以有效地排序，
最终被插入排序。

最差时间复杂度	O(nlog2^2 n)
最优时间复杂度	O(n)
平均时间复杂度	根据步长序列的不同而不同。

'''
import math

def shell(array):
    h = 1
    while h < int(math.floor(len(array)/3)):
        h = 3*h + 1

    while h >= 1:
        for i in range(h, len(array)):
            insertion = array[i]
            j = i
            while j > 0 and insertion < array[j-h]:
                array[j] = array[j-h]
                j -= h
            array[j] = insertion
        h = int(math.floor(h/3))
    return array


if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    input = getRandomNumbers(0, 10000, 100)

    print shell(input)
