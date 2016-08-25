#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Merge sort

归并排序
'''

def merge(array, lo, mid, hi):
    # merge array[lo..mid] and array[mid..hi]
    i = lo
    j = mid + 1

    aux = array[:] # copy the array to aux

    for k in range(len(array)):
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > hi:
            array[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1

    return array

if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    input = getEscRandomNumbers(0, 1000, 10) + getEscRandomNumbers(0, 1000, 10)

    print merge(input, 0, 8, len(input)-1)
