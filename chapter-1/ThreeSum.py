#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        cnt = 0
        result = []
        for i in range(len(input)):
            for j in range(i+1, len(input)):
                for k in range(j+1, len(input)):
                    if input[i] + input[j] + input[k] == 0:
                        result.append([input[i], input[j], input[k]])
                        cnt += 1
        print 'count: %d,  array: %s' % (cnt, result)


class TwoSum(object):

    def count(self, input):
        cnt = 0
        result = []
        for i in range(len(input)):
            for j in range(i+1, len(input)):
                if input[i] + input[j] == 0:
                    result.append([input[i], input[j]])
                    cnt += 1
        print 'count: %d,  array: %s' % (cnt, result)

    def countFast(self, input):
        cnt = 0
        result = []
        input.sort()
        for i in range(len(input)):
            if BinarySearch(input, -input[i]) > i:
                cnt += 1
                result.append([input[i], -input[i]])
        print 'count: %d,  array: %s' % (cnt, result)

threesum = ThreeSum()
twosum = TwoSum()
input = [-1, -2, -5, 1, 3, -2, 0, 2]
twosum.count(input)
twosum.countFast(input)
