#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Algorithms Pracitice: ThreeSum question
A program with cubic running time. Reads n integers and counts the number of
triples that sum to exactly 0 (Intergers are different in this array)
算法训练： 三元和的问题
统计所有和为 0 的三整数元组的数量（数组内整数均不相等）
'''

from time import time

def BinarySearch(input, key):
    lo = 0
    hi = len(input) - 1
    while(lo <= hi):
        mid = int(lo + (hi-lo) / 2)
        if (key < input[mid]):
            hi = mid - 1
        elif (key > input[mid]):
            lo = mid + 1
        else:
            return mid
    return -1


class ThreeSum(object):
    """docstring for ThreeSum."""

    def count(self, input):
        start = time()
        cnt = 0
        result = []

        for i in range(len(input)):
            for j in range(i+1, len(input)):
                for k in range(j+1, len(input)):
                    if input[i] + input[j] + input[k] == 0:
                        result.append([input[i], input[j], input[k]])
                        cnt += 1
        end = time()
        print 'time: %s, count: %d,  array: %s' % (end - start, cnt, result)

    def countFast(self, input):
        start = time()
        cnt = 0
        result = []
        input.sort()

        for i in range(len(input)):
            for j in range(i+1, len(input)):
                if BinarySearch(input, -input[i]-input[j]) > j:
                    result.append([input[i], input[j], -input[i]-input[j]])
                    cnt += 1
        end = time()
        print 'time: %s, count: %d,  array: %s' % (end - start, cnt, result)


class TwoSum(object):

    def count(self, input):

        start = time()
        cnt = 0
        result = []

        for i in range(len(input)):
            for j in range(i+1, len(input)):
                if input[i] + input[j] == 0:
                    result.append([input[i], input[j]])
                    cnt += 1
        end = time()
        print 'time: %s, count: %d,  array: %s' % (end - start, cnt, result)

    def countFast(self, input):
        start = time()
        cnt = 0
        result = []
        input.sort()

        for i in range(len(input)):
            if BinarySearch(input, -input[i]) > i:
                result.append([input[i], -input[i]])
                cnt += 1
        end = time()
        print 'time: %s, count: %d,  array: %s' % (end - start, cnt, result)

threesum = ThreeSum()
twosum = TwoSum()
input = [-1, -2, -5, 1, 0, 2, 10, 23, -6, 42, 3, 22, -10, 40, 41, 55, \
11, -14, -5, -3, 90, 19, 13, -22, 33, 7, -8, 9, 25, -29, 66, 43, -60, \
80, 88, 100, -200, -300, 567, 322, 102, 569, 321, 221, 240, 432, 564, \
-222, -444, 143, 654, 323, 76, 54, -87, -44]
# twosum.count(input)
# twosum.countFast(input)
threesum.count(input)
threesum.countFast(input)
