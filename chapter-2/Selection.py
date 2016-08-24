#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Selection sort.

One of the simplest sorting algorithms works as follows: First,
find the smallest item in the array, and exchange it with the first entry. Then,
find the next smallest item and exchange it with the second entry. Continue in
this way until the entire array is sorted. This method is called selection sort
because it works by repeatedly selecting the smallest remaining item.

Average case performance О(n^2)

选择排序

一种最简单的排序算法是这样的，首先找到数组中最小的元素，其次，将它和数组的第一个元素交换位置。
再次，在剩下的元素找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。

时间复杂度 O(n^2)
'''
def selection(array):
    if len(array) == 1:
        return array

    for i in range(len(array)-1):
        minIndex = i

        # select the minumun item in unsorted arrays
        for j in range(i+1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j

        # swap the items
        array[i], array[minIndex] = array[minIndex], array[i]

    return array

array = [0, 2, 4, 5, 1, 10, 9, 42, 1, 4, 11, 15, 16, 13]
print selection(array)
