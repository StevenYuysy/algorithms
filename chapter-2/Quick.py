#! usr/bin/pyhton
# -*- coding: utf-8 -*-

"""
Qiuck Sort

Quicksort is a divide-and-conquer method for sorting. It works by partitioning
an array into two parts, then sorting the parts independently.

Average performance O(nlogn)

快速排序

快速排序是一种分治的排序算法。它将一个数组分成两个子数组，将两部分独立地排序。

平均时间复杂度 O(nlogn)
"""

def quicksort(array):

    def sort(lo, hi):
        if (hi <= lo): return
        j = partition(lo, hi)
        sort(lo, j-1)
        sort(j+1, hi)


    def partition(lo, hi):
        i = lo + 1
        j = hi
        v = array[lo] # Base number
        while True:
            while array[i] < v:
                if i == hi: break
                i += 1
            while array[j] > v:
                if j == lo: break
                j -= 1
            if i >= j: break
            array[i], array[j] = array[j], array[i]
        array[lo], array[j] = array[j], array[lo]
        return j

    sort(0, len(array)-1)
    return array

if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    input = getRandomNumbers(0, 10000, 100)
    print quicksort(input)
