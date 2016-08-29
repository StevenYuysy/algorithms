#! usr/bin/python
# -*- coding: utf-8 -*-
"""
Insertion

The algorithm that people often use to sort bridge hands is to consider the
cards one at a time, inserting each into its proper place among those already
considered (keeping them sorted). In a computer implementation, we need to make
space for the current item by moving larger items one position to the right,
before inserting the current item into the vacated position.

Average case performance О(n^2)

插入排序
通常人们整理桥牌的方法是一张一张的来，将每一张牌插入到其他已经有序的牌中的适当位置。在计算机的实
现中，为了给更小的元素腾出空间，我们需要将其余所有元素在插入之前都向右移动一位。

时间复杂度 O(n^2)
"""

def insertion(array):
    if len(array) == 1:
        return array

    for i in range(1, len(array)):
        insertion = array[i]
        j = i

        # check the right position to insert forwardly and move the position of
        # larger item
        while j > 0 and insertion < array[j-1]:
            array[j] = array[j-1]
            j -= 1

        # insert the right position
        array[j] = insertion

    return array

if __name__ == "__main__":

    import sys
    sys.path.append('../')
    from generator import *

    input = getRandomNumbers(0, 10000, 100)

    print insertion(input)
