#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Merge sort
Average case performance O(nlogn)

归并排序
平均时间复杂度	O(nlogn)
"""

def merge(array, lo, mid, hi):
    """Abstract in-place merge.

     The method merge(a, lo, mid, hi) puts the results of merging the subarrays
     a[lo..mid] with a[mid+1..hi] into a single ordered array, leaving the
     result in a[lo..hi].

     Args:
        array: The array that need to be sorted.
        lo: The begin index of the first sorted array.
        mid: The begin index of the second sorted array.
        hi: The end of the index.

    Returns:
        array: The sorted array.

    """
    # merge array[lo..mid] and array[mid..hi]
    i = lo
    j = mid + 1

    aux = array[:] # copy the array to aux

    for k in range(lo, hi+1): # actually we need to change at least 2 times!
        # run out of the left side array
        if i > mid:
            array[k] = aux[j]
            j += 1
        # run out of the right side array
        elif j > hi:
            array[k] = aux[i]
            i += 1
        # put the less one to the array
        elif aux[i] > aux[j]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1
    return array

def sort(array, lo, hi):

    """Top-down mergesort.

    A recursive mergesort implementation based on this abstract in-place merge.

    Args:
        array: The array that need to be sorted.
        lo: The begin index of the array.
        hi: The end index of the array.

    Returns:
        array: The sorted array from lo to hi.

    """

    if hi <= lo: return
    mid = lo + (hi - lo) // 2
    sort(array, lo, mid)
    sort(array, mid+1, hi)
    print('merge(array, %s, %s, %s)' % (lo, mid, hi))
    return merge(array, lo, mid, hi)

def sortBU(array):

    """ Bottom-up mergesort.

    Another way to implement mergesort is to organize the merges so that we
    do all the merges of tiny arrays on one pass, then do a second pass to merge
    those arrays in pairs, and so forth, continuing until we do a merge that
    encompasses the whole array.

    Args:
        array: The array that need to be sorted.

    Returns:
        array: The sorted array.
    """

    sz = 1
    N = len(array)
    result = []
    while sz < N:
        lo = 0
        while lo < N - sz:
            print('sz : %s, merge(array, %s, %s, %s)' \
             % (sz, lo, lo+sz-1, min(int(lo+sz+sz-1), int(N-1))))
            result = merge(array, lo, lo+sz-1, min(int(lo+sz+sz-1), int(N-1)))[:]
            lo += sz + sz
        sz = sz + sz
    return result

if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    input = getRandomNumbers(0, 1000, 16)
    print('type: sort from top 2 bottom: %s' % sort(input, 0, len(input)-1))
    print('type: sort form bottom 2 top %s' % sortBU(input))
